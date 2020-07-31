from slmigrate import constants
from test import test_constants
import json
import subprocess
import os

def get_service_config(service, test=False):
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name + ".json")
    if test:
        config_file = os.path.join(os.getcwd(), "test", "test_service.json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        return json.load(json_file)


def migrate_mongo_cmd(service, action, config):
    # config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service.name + ".json")
    # with open(config_file, encoding='utf-8-sig') as json_file:
    #     config = json.load(json_file)
    # config = get_service_config(service)
    mongo_dump_file = os.path.join(constants.no_sql_dump_dir, config[service.name]['Mongo.Database'])
    if action == constants.capture_arg:
        cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip"
    if action == constants.restore_arg:
        cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file)
    subprocess.run(cmd_to_run)


def start_mongo(mongod_exe, mongo_config):
    mongo_process = subprocess.Popen(mongod_exe + " --config " + '"' + str(mongo_config) + '"', creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)
    # mongo_process = subprocess.Popen(mongod_exe + " --config " + '"' + str(mongo_config) + '"')
    return mongo_process


def stop_mongo(proc):
    subprocess.Popen.kill(proc)
