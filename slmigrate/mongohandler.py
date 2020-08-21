from slmigrate import constants
import json
import subprocess
import os


def get_service_config(service, test=False):
    config_file = os.path.join(constants.service_config_dir, service.name + ".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        return json.load(json_file)


def migrate_mongo_cmd(service, action, config):
    mongo_migration_dir = os.path.join(constants.migration_dir, "mongo-dump")
    mongo_dump_file = os.path.join(mongo_migration_dir, config[service.name]['Mongo.Database'])
    if action == constants.capture_arg:
        cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + mongo_migration_dir + " --gzip"
    if action == constants.restore_arg:
        cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(cmd_to_run)


def start_mongo(mongod_exe, mongo_config):
    mongo_process = subprocess.Popen(mongod_exe + " --config " + '"' + str(mongo_config) + '"', creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)
    return mongo_process


def stop_mongo(proc):
    subprocess.Popen.kill(proc)
<<<<<<< Updated upstream
=======


def capture_migration(service, action, config):
    if action != constants.capture_arg:
        return
    cmd_to_run = constants.mongo_dump + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --out " + constants.mongo_migration_dir + " --gzip"
    subprocess.run(cmd_to_run)


def restore_migration(service, action, config):
    if action != constants.restore_arg:
        return
    mongo_dump_file = os.path.join(constants.mongo_migration_dir, config[service.name]['Mongo.Database'])
    cmd_to_run = constants.mongo_restore + " --port " + str(config[service.name]['Mongo.Port']) + " --db " + config[service.name]['Mongo.Database'] + " --username " + config[service.name]['Mongo.User'] + " --password " + config[service.name]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(cmd_to_run)


def copy_or_merge_taghistory_metadata(source_db, destination_db):
    # check if workspace and paths match, don't migrate, but cache id
    # if they dont match try and move the document to destination db
    return id_cache


def copy_or_merge_taghistory_values(source_db, destination_db, id_cache):
    # go through the _id cache and update to destination metadata ids for history documents coming from source db
    pass


def migrate_within_instance(service, action, config):
    if not action == constants.thdbbug.arg:
        return
    codec = bson.codec_options.CodecOptions(uuid_representation=bson.binary.UUID_SUBTYPE)
    no_sql_config = get_service_config(constants.no_sql)
    client = MongoClient(host=[no_sql_config[constants.no_sql.name]['Mongo.Host']], port=no_sql_config[constants.no_sql.name]['Mongo.Port'], username=no_sql_config[constants.no_sql.name]['Mongo.User'], password=no_sql_config[constants.no_sql.name]['Mongo.Password'])
    source_db = client.get_database(name=constants.source_db, codec_options=codec)
    destination_db = client.get_database(name=service.destination_db, codec_options=codec)

    for collection in service.collections_to_migrate:
        if collection == 'metatdata':
            id_cache = copy_or_merge_taghistory_metadata(source_db, destination_db)
        
        source_collection = source_db.get_collection(collection).find()
        destination_collection = destination_db.get_collection(collection)
        for document in source_collection:
            try:
                print("Migrating " + str(document['_id']))
                # if migrating metadata document has same workspace+tag path don't migrate that document. Do migrate the history but mutate the value document to use the metadata idea from the existing metadata document
                if source_collection.find('$and': [{_id: document['_id'], '$and': [{'workspace': "foo" }, {'path': "bar"}]}]) != destination_collection.find('$and': [{workspace: "foo" }, {path: "bar"}]})
                    try:
                        destination_collection.insert_one(document)
                    except pyerr.DuplicateKeyError:
                    print("Docuement " + str(document['_id']) + " already exists. Skipping")
                else: #merge the documents together? Create a cache of _ids where this is the case so they can be used to look up and replace in the values collection. 


            # if metadata workspace and path match don't move the document
            destination_collection.update_one({$and: [{"workspace": { $eq: document.workspace}}, { $eq "path":}, {$set: {}},)


def migrate_mongo_cmd(service, action, config):
    if action == constants.thdbbug.arg:
        migrate_within_instance(service, action, config)
    if action == constants.capture_arg:
        capture_migration(service, action, config)
    if action == constants.restore_arg:
        restore_migration(service, action, config)
>>>>>>> Stashed changes
