# migrate-from-fis.py

# This example will generate a migration directory containing all file ingested by a SystemLink Server.  

import os, subprocess, json, shutil

# Set variables for various paths used during migration
migration_dir = "C:\migration"
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
prorgram_data_dir = os.environ.get("ProgramData")
fis_data_source_dir = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "Data", "FileIngestion")
fis_data_migration_dir = os.path.join(migration_dir, "FileIngestion")
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")

# Get data from service's json config file 
service= "FileIngestion"
config_file = os.path.join(prorgram_data_dir, "National Instruments", "Skyline", "Config", service+".json")
with open(config_file, encoding='utf-8-sig') as json_file:
    config = json.load(json_file)

# Dump mongo database to migration directory
mongo_dump_cmd = mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + no_sql_dump_dir + " --gzip"
subprocess.run(mongo_dump_cmd)

# Copy ingested files to migration direction 
migration_files = os.listdir(fis_data_source_dir)
for file_name in migration_files:
    full_file_path = os.path.join(fis_data_source_dir, file_name)
    if os.path.isfile(full_file_path):
        shutil.copy(full_file_path, fis_data_migration_dir)