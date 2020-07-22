import os, subprocess, json

migration_directory = "C:\migration"
no_sql_dump_dir = os.path.join(migration_directory, "mongo-dump")

program_file_dir = os.environ.get("ProgramW6432")
prorgram_data_dir = os.environ.get("ProgramData")
mongo_restore = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongorestore.exe")

service = "TestMonitor"
config_file = os.path.join(prorgram_data_dir, "National Instruments", "Skyline", "Config", service+".json")

with open(config_file, encoding='utf-8-sig') as json_file:
    config = json.load(json_file)

mongo_dump_file = os.path.join(no_sql_dump_dir, config[service]['Mongo.Databases'])

mongo_restore_cmd = mongo_restore + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --gzip " + mongo_dump_file
subprocess.run(mongo_restore_cmd)