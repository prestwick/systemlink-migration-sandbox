from slmigrate import constants
import json, subprocess

def capture_mongo_data(service):
    print (service + " capture_mongo_data_called")
    config_file = os.path.join(program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)
        # Dump mongo database to migration directory
        mongo_dump_cmd = mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + no_sql_dump_dir + " --gzip"
        subprocess.run(mongo_dump_cmd)
    
def capture_file_data(service):
    print (service + " capture_file_data called")


def capture_migration(service):
    print(service + " capture migration called")
    capture_mongo_data(service)
    if (service == constants.opcservice):
        capture_file_data(service)



    
