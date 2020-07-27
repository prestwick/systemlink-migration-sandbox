from slmigrate import constants
import json, subprocess, os, sys, shutil

# capture_module = sys.modules[__name__]

def capture_mongo_data(service):
    print (service + " capture_mongo_data_called")
    config_file = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
        # Dump mongo database to migration directory
        mongo_dump_cmd = constants.mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + constants.no_sql_dump_dir + " --gzip"
        subprocess.run(mongo_dump_cmd)
    
def check_migration_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir)

def capture_file_data(source, dest):
    print ("capture_file_data called")
    check_migration_dir(dest)
    shutil.copytree(source, dest)   

def capture_redis_dump():
    print("Stopping Tag service")
    subprocess.run(constants.slconf_cmd_stop_tag)
    # Replace the contents of the current Redis DB instance. This will remove previously created tags from the server. 
    check_migration_dir(constants.keyvaluedb_migration_dir)
    os.mkdir(constants.keyvaluedb_migration_dir)
    shutil.copy(constants.keyvaluedb_dump_source, constants.keyvaluedb_migration_dir)
    print ("Starting all SystemLink services")
    subprocess.run(constants.slconf_cmd_start)


#     os.mkdir(keyvaluedb_migration_dir)
# shutil.copy(keyvaluedb_dump_source, keyvaluedb_migration_dir)

# def capture_OpcClient_file_data():
#     print ("capture_opc_file_data called")


def capture_migration(service):
    print(service + " capture migration called")
    capture_mongo_data(service)
    if (service == constants.opc_service):
        capture_file_data(constants.opc_cert_source_dir, constants.opc_cert_migration_dir)
        # getattr(capture_module, 'capture_' + service + '_file_data')()
    if (service == constants.file_sevice):
        capture_file_data(constants.fis_data_source_dir, constants.fis_data_migration_dir)
    if (service == constants.taghistorian_service):
        capture_redis_dump()

    # else:
        # capture_file_data(service)



    
