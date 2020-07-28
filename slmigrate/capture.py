from slmigrate import constants
import json, subprocess, os, sys, shutil

def capture_mongo_data(service):
    print (service['service'] + " capture_mongo_data_called")
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service['service'] +".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
        subprocess.run(constants.mongo_dump + " --port " + str(config[service['service']]['Mongo.Port']) + " --db " + config[service['service']]['Mongo.Database'] + " --username " + config[service['service']]['Mongo.User'] + " --password " + config[service['service']]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip")
        
def check_migration_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir)

def capture_dir_data(service):
    print ("capture_dir_data called")
    # check_migration_dir(dest)
    check_migration_dir(service['migration_dir'])
    # shutil.copytree(source, dest) 
    shutil.copytree(service['source_dir'], service['migration_dir'])  

def capture_singlefile(service):
    check_migration_dir(service['singlefile_migration_dir'])
    os.mkdir(service['singlefile_migration_dir'])
    shutil.copy(service['singlefile_to_migrate'], service['singlefile_migration_dir'])

def capture_migration(service):
    print(service['service'] + " capture migration called")
    capture_mongo_data(service)
    if service['service_require_restarts']:
        print("Stopping " +  service['service'] + " service")
        subprocess.run(constants.slconf_cmd_stop_service + service['service'])
    if (service['directory_migration']):
        capture_dir_data(service)
    if (service['singlefile_migration']):
        capture_singlefile(service)
    if service['service_require_restarts']:
        print ("Starting " + service['service'] + " service")
        subprocess.run(constants.slconf_cmd_start_service + service['service'])