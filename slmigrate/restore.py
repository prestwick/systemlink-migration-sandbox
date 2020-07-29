from slmigrate import constants, common
import json, subprocess, os, sys, shutil
from distutils.dir_util import copy_tree

# def restore_mongo_data(service):
#     config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name +".json")
#     with open(config_file, encoding='utf-8-sig') as json_file:
#         config = json.load(json_file)
#         mongo_dump_file = os.path.join(constants.no_sql_dump_dir, config[service.name]['Mongo.Database'])
#         subprocess.run(constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file)

def restore_dir_data(service):
    if  not service.directory_migration:
        return
    copy_tree(service.migration_dir, service.source_dir)

def restore_singlefile(service):
    if not service.singlefile_migration:
        return
    singlefile_full_path = os.path.join(service.singlefile_migration_dir, service.singlefile_to_migrate) 
    shutil.copy(singlefile_full_path, service.singlefile_source_dir)

def restore_migration(service):
    print(service.name + " restore migration called")
    common.execute_mongo_cmd(service.name, constants.restore_arg)
    common.stop_sl_service(service)
    restore_dir_data(service)
    restore_singlefile(service)
    common.start_all_sl_services(service)