from slmigrate import constants
from distutils import dir_util
import json, subprocess, os, sys, shutil

#something is wrong with both capture and restore
def migrate_mongo_cmd(service, action):
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name +".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
    mongo_dump_file = os.path.join(constants.no_sql_dump_dir, config[service.name]['Mongo.Database'])
    if action == constants.capture_arg:
        cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip"
    elif action == constants.restore_arg:
        cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file)

    
    subprocess.run(cmd_to_run)

def stop_sl_service(service):
    if service.require_service_restart:
        print("Stopping " +  service.service_to_restart + " service")
        subprocess.run(constants.slconf_cmd_stop_service + service.service_to_restart + " wait")
    
def start_all_sl_services(service):
    if service.require_service_restart:
        print ("Starting " + service.service_to_restart + " service")
        subprocess.run(constants.slconf_cmd_start_all)

def check_migration_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir)

def migrate_singlefile(service, action):
    if  not service.singlefile_migration:
        return
    if action == constants.capture_arg:
        check_migration_dir(service.singlefile_migration_dir)
        os.mkdir(service.singlefile_migration_dir)
        singlefile_full_path = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", service.singlefile_to_migrate)
        shutil.copy(singlefile_full_path, service.singlefile_migration_dir)
    elif action == constants.restore_arg:
        singlefile_full_path = os.path.join(service.singlefile_migration_dir, service.singlefile_to_migrate) 
        shutil.copy(singlefile_full_path, service.singlefile_source_dir)

def migrate_dir(service, action):
    if not service.directory_migration:
        return
    if action == constants.capture_arg:
        check_migration_dir(service.migration_dir)
        shutil.copytree(service.source_dir, service.migration_dir) 
    elif action == constants.restore_arg:
        dir_util.copy_tree(service.migration_dir, service.source_dir)

def migrate(service, action):
    print(service.name + " " + action + " migration called")
    migrate_mongo_cmd(service, constants.capture_arg)
    stop_sl_service(service)
    migrate_dir(service, action)
    migrate_singlefile(service, action)
    start_all_sl_services