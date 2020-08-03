import os
import shutil
import slmigrate.constants as constants
import slmigrate.mongohandler as mongohandler
import slmigrate.arghandler as arghandler
import slmigrate.filehandler as filehandler
from test import test_constants
from types import SimpleNamespace


def test_parse_arguments():
    parser = arghandler.parse_arguments([constants.tag.arg, constants.opc.arg, constants.fis.arg, constants.alarmrule.arg, constants.testmonitor.arg])
    assert parser.parse_known_args()


def test_capture_migrate_mongo_data():
    constants.mongo_config = test_constants.mongo_config
    constants.mongo_dump = test_constants.mongo_dump
    constants.mongo_restore = test_constants.mongo_restore
    constants.migration_dir = test_constants.migration_dir
    constants.service_config_dir = test_constants.service_config_dir
    mongo_process = mongohandler.start_mongo(test_constants.mongod_exe, test_constants.mongo_config)
    test_service = test_constants.test_service
    if os.path.isdir(constants.migration_dir):
        shutil.rmtree(constants.migration_dir)
    config = mongohandler.get_service_config(test_service, False)
    mongohandler.migrate_mongo_cmd(test_service, constants.capture_arg, config)
    dump_dir = os.path.join(constants.migration_dir, "local")
    mongohandler.stop_mongo(mongo_process)
    assert dump_dir


def check_migration_dir():
    test_dir = os.mkdir(os.path.join(os.path.abspath(os.sep)), "test_dir")
    filehandler.check_migration_dir(test_dir)
    assert not os.path.isdir(test_dir)


def test_capture_migrate_dir():
    test = test_constants.test_service
    constants.migration_dir = test_constants.migration_dir
    if os.path.isdir(test.migration_dir):
        shutil.rmtree(test.migration_dir)
    if os.path.isdir(test.source_dir):
        shutil.rmtree(test.source_dir)
    os.mkdir(test.source_dir)
    os.mkdir(os.path.join(test.source_dir, "lev1"))
    os.mkdir(os.path.join(test.source_dir, "lev1", "lev2"))
    filehandler.migrate_dir(test, constants.capture_arg)
    assert os.path.isdir(os.path.join(constants.migration_dir, test.name, "lev1", "lev2"))
    shutil.rmtree(test.source_dir)
    shutil.rmtree(constants.migration_dir)



def test_capture_migrate_singlefile():
    constants.migration_dir = test_constants.migration_dir
    test = test_constants.test_service
    if os.path.isdir(test.singlefile_migration_dir):
        shutil.rmtree(test.singlefile_migration_dir)
    if os.path.isdir(test.singlefile_source_dir):
        shutil.rmtree(test.singlefile_source_dir)
    os.mkdir(test.singlefile_source_dir)
    os.mkdir(constants.migration_dir)
    test_file = open(os.path.join(test.singlefile_source_dir, "demofile2.txt"), "a")
    test_file.close()
    filehandler.migrate_singlefile(test, constants.capture_arg)
    assert os.path.isfile(os.path.join(test.migration_dir,  "demofile2.txt"))
    shutil.rmtree(test.source_dir)
    shutil.rmtree(constants.migration_dir)
