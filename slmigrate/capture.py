from slmigrate import constants, common
import json, subprocess, os, sys, shutil

# def capture_mongo_data(service):
#     config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name +".json")
#     with open(config_file, encoding='utf-8-sig') as json_file:
#         config = json.load(json_file)
#         subprocess.run(constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip")
        
def check_migration_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir)

def capture_dir_data(service):
    if not service.directory_migration:
        return
    check_migration_dir(service.migration_dir)
    shutil.copytree(service.source_dir, service.migration_dir)  

def capture_singlefile(service):
    if  not service.singlefile_migration:
        return
    check_migration_dir(service.singlefile_migration_dir)
    os.mkdir(service.singlefile_migration_dir)
    singlefile_full_path = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", service.singlefile_to_migrate)
    shutil.copy(singlefile_full_path, service.singlefile_migration_dir)

def capture_migration(service):
    print(service.name + " capture migration called")
    common.execute_mongo_cmd(service.name, constants.capture_arg)
    common.stop_sl_service(service)
    capture_dir_data(service)
    capture_singlefile(service)
    common.start_all_sl_services