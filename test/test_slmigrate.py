import os
import shutil
import slmigrate.constants as constants
import slmigrate.mongohandler as mongohandler
import slmigrate.arghandler as arghandler
import slmigrate.filehandler as filehandler
from types import SimpleNamespace


def test_parse_arguments():
    parser = arghandler.parse_arguments([constants.tag.arg, constants.opc.arg, constants.fis.arg, constants.alarmrule.arg, constants.testmonitor.arg])
    assert parser.parse_known_args()


def test_capture_migrate_mongo_data():
    mongo_process = mongohandler.start_mongo()
    test_service = constants.alarmrule
    if os.path.isdir(constants.migration_dir):
        shutil.rmtree(constants.migration_dir)
    mongohandler.migrate_mongo_cmd(test_service, constants.capture_arg)
    dump_dir = os.path.join(constants.migration_dir, "nitagrule")
    mongohandler.stop_mongo(mongo_process)
    assert dump_dir


def check_migration_dir():
    test_dir = os.mkdir(os.path.join(os.path.abspath(os.sep)), "test_dir")
    filehandler.check_migration_dir(test_dir)
    assert not os.path.isdir(test_dir)


def test_capture_migrate_dir():
    test_dict = {
        'arg': 'test',
        'service_nanme': "test",
        'directory_migration': True,
        'singlefile_migration': False,
        'require_service_restart': False,
        'migration_dir': os.path.join(os.path.abspath(os.sep), "mig_test_dir"),
        'source_dir': os.path.join(os.path.abspath(os.sep), "source_test_dir")
    }
    test = SimpleNamespace(**test_dict)
    if os.path.isdir(test.migration_dir):
        shutil.rmtree(test.migration_dir)
    if os.path.isdir(test.source_dir):
        shutil.rmtree(test.source_dir)
    os.mkdir(test.migration_dir)
    os.mkdir(test.source_dir)
    os.mkdir(os.path.join(test.source_dir, "lev1"))
    os.mkdir(os.path.join(test.source_dir, "lev1", "lev2"))
    filehandler.migrate_dir(test, constants.capture_arg)
    assert os.path.isdir(os.path.join(test.migration_dir, "lev1", "lev2"))


def test_capture_migrate_singlefile():
    test_dict = {
        'arg': 'test',
        'service_nanme': "test",
        'directory_migration': False,
        'singlefile_migration': True,
        'require_service_restart': False,
        'singlefile_migration_dir': os.path.join(os.path.abspath(os.sep), "migration_test_dir"),
        'singlefile_source_dir': os.path.join(os.path.abspath(os.sep), "source_test_dir"),
        'singlefile_to_migrate': os.path.join(os.path.abspath(os.sep), "source_test_dir", "demofile2.txt")
    }
    test = SimpleNamespace(**test_dict)
    if os.path.isdir(test.singlefile_migration_dir):
        shutil.rmtree(test.singlefile_migration_dir)
    if os.path.isdir(test.singlefile_source_dir):
        shutil.rmtree(test.singlefile_source_dir)
    os.mkdir(test.singlefile_migration_dir)
    os.mkdir(test.singlefile_source_dir)
    test_file = open(os.path.join(test.singlefile_source_dir, "demofile2.txt"), "a")
    test_file.close()
    filehandler.migrate_singlefile(test, constants.capture_arg)
    assert os.path.isfile(os.path.join(test.singlefile_migration_dir, "demofile2.txt"))
