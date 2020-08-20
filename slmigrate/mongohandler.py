from slmigrate import constants
import json
import subprocess
import os
from pymongo import MongoClient


def get_service_config(service):
    config_file = os.path.join(constants.service_config_dir, service.name + ".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        return json.load(json_file)


def start_mongo(mongod_exe, mongo_config):
    mongo_process = subprocess.Popen(mongod_exe + " --config " + '"' + str(mongo_config) + '"', creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)
    return mongo_process


def stop_mongo(proc):
    subprocess.Popen.kill(proc)


def capture_migration(service, action, config):
    if action != constants.capture_arg:
        return
    mongo_migration_dir = os.path.join(service.migration_dir, "mongo-dump")
    cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + mongo_migration_dir + " --gzip"
    subprocess.run(cmd_to_run)


def restore_migration(service, action, config):
    mongo_migration_dir = os.path.join(service.migration_dir, "mongo-dump")
    mongo_dump_file = os.path.join(mongo_migration_dir, config[service.name]['Mongo.Database'])
    if action != constants.restore_arg:
        return
    cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(cmd_to_run)


def migrate_within_instance(service, action, config):
    if not action == constants.thdbbug.arg:
        return
    # TODO build up DB string
    no_sql_config = get_service_config(constants.no_sql.name)
    # Below will alays defualt to authSource=admin
    client = MongoClient(host=[no_sql_config[constants.no_sql.name]['Mongo.Host']], port=no_sql_config[constants.no_sql.name]['Mongo.Port'], username=no_sql_config[constants.no_sql.name]['Mongo.user'], password=no_sql_config[constants.no_sql.name]['Mongo.Password'])
    admin_db = client.get_database(name='admin')
    taghistorian_db = client.get_database(name='nitaghistorian')
    admin_metadata_collection = admin_db.get_collection('metadata').find()
    # TODO db.source_collection.find({condition}).forEach(function(d){ db.getSiblingDB('target_database')['target_collection'].insert(d); });

    for document in admin_metadata_collection:
        taghistorian_db.get_collection('metadata').insert(document)



    # db.source_collection.find({condition}).forEach(
    #     function(d){ 
    #         db.getSiblingDB('target_database')['target_collection'].insert(d); 
    #         }
    #     );



def migrate_mongo_cmd(service, action, config):
    migrate_within_instance(service, action, config)
    capture_migration(service, action, config)
    restore_migration(service, action, config)
