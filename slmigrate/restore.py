from slmigrate import constants
import json, subprocess, os, sys, shutil
from distutils.dir_util import copy_tree

def restore_mongo_data(service):
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name +".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
        mongo_dump_file = os.path.join(constants.no_sql_dump_dir, config[service.name]['Mongo.Database'])
        subprocess.run(constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file)


def restore_dir_data(service):
    # check_migration_dir(dest)
    # check_migration_dir(service.migration_dir)
    # shutil.copytree(service.migration_dir, service.source_dir)
    copy_tree(service.migration_dir, service.source_dir)
    #Above coud fail if dir is already there

def restore_singlefile(service):
    # check_migration_dir(service.singlefile_migration_dir)
    # os.mkdir(service.singlefile_migration_dir)
    singlefile_full_path = os.path.join(service.singlefile_migration_dir, service.singlefile_to_migrate) 
    shutil.copy(singlefile_full_path, service.singlefile_source_dir)
    #Above coud fail if file is already there


def restore_migration(service):
    print(service.name + " restore migration called")
    restore_mongo_data(service)
    # Consider puting if statements within functions 
    if service.require_service_restart:
        print("Stopping " +  service.name + " service")
        subprocess.run(constants.slconf_cmd_stop_service + service.name)
    if (service.directory_migration):
        restore_dir_data(service)
    if (service.singlefile_migration):
        restore_singlefile(service)
    if service.require_service_restart:
        print ("Starting " + service.name + " service")
        subprocess.run(constants.slconf_cmd_start_service + service.name)