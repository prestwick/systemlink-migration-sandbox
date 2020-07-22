# migrate-from-test-data.py

# This example will generate a migration directory containing test data ingested via the SystemLink Test Monitor service. 
# This script does not migrate files associated with test results

import os, subprocess, json

# Set variables for various paths used during migration
migration_directory = "C:\migration"
no_sql_dump_dir = os.path.join(migration_directory, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")

# Get data from service's json config file 
service= "TestMonitor"
config_file = os.path.join(program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
with open(config_file, encoding='utf-8-sig') as json_file:
    config = json.load(json_file)

# Dump mongo database to migration directory
mongo_dump_cmd = mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + no_sql_dump_dir + " --gzip"
subprocess.run(mongo_dump_cmd)