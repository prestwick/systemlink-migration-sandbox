# migrate-to-alarm-rules.py

# This example will migrate all tag alarm rules generated from running migrate-from-alarms.ps1 to another SystemLink Server
# This script does not migrate tags associated with alarms, or  the alarm instances generated from these rule. 

import os, subprocess, json

# Set variables for various paths used during migration
migration_directory = "C:\migration"
no_sql_dump_dir = os.path.join(migration_directory, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")
mongo_restore = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongorestore.exe")
#$SlConfCmd = Join-Path $env:ProgramFiles "National Instruments" Shared Skyline NISystemLinkServerConfigCmd.exe
slconf_cmd = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NISystemLinkServerConfigCmd.exe")
print(slconf_cmd)


# Get data from service's json config file 
service = "TagRuleEngine"
config_file = os.path.join(program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
with open(config_file, encoding='utf-8-sig') as json_file:
    config = json.load(json_file)

# Restore mongo database from contents of migration directory
mongo_dump_file = os.path.join(no_sql_dump_dir, config[service]['Mongo.Database'])
mongo_restore_cmd = mongo_restore + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --gzip " + mongo_dump_file
subprocess.run(mongo_restore_cmd)

# Restart service manager to access alarm rule details
slconf_cmd_stop = slconf_cmd + " stop-all-services" + " wait"
slconf_cmd_start = slconf_cmd + " start-all-services"
subprocess.run(slconf_cmd_stop)
subprocess.run(slconf_cmd_start)