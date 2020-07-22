import os, subprocess, json

migration_directory = "C:\migration"
no_sql_dump_dir = os.path.join(migration_directory, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
prorgram_data_dir = os.environ.get("ProgramData")
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")


service= "TestMonitor"
config_file = os.path.join(prorgram_data_dir, "National Instruments", "Skyline", "Config", service+".json")

with open(config_file, encoding='utf-8-sig') as json_file:
    config = json.load(json_file)

mongo_dump_cmd = mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + no_sql_dump_dir + " --gzip"
print (mongo_dump_cmd)
subprocess.run(mongo_dump_cmd)