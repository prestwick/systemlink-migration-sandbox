from slmigrate import constants
import json, subprocess, os, sys, shutil

def execute_mongo_cmd(service, action):
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name +".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
    mongo_dump_file = os.path.join(constants.no_sql_dump_dir, config[service.name]['Mongo.Database'])
    if action == constants.capture_arg:
        cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip"
    elif action:
        cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(cmd_to_run)

def stop_sl_service(service):
    if service.require_service_restart:
        print("Stopping " +  service.service_to_restart + " service")
        subprocess.run(constants.slconf_cmd_stop_service + service.service_to_restart + " wait")
    
def start_all_sl_services(service):
    if service.require_service_restart:
        print ("Starting " + service.service_to_restart + " service")
        subprocess.run(constants.slconf_cmd_start_all)
