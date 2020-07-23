# migrate-to-opcua-tags.py

# This example will migrate all tags, tag histories, OPCUA session, and OPCUA certificates generated from running migrate-from-opcua-tags.ps1 to another SystemLink Server
# This script will migrate all tags, not just those created by OPCUA session monitors. 

import os, subprocess, json, shutil

# Set variables for various paths used during migration
migration_dir = "C:\migration"
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")
# opc_migration_dir= os.path.join(migration_dir, "OpcClient")
sl_data_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data")
# opc_cert_source_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "OpcClient")
opc_cert_migration_dir = os.path.join(migration_dir, "OpcClient")
keyvaluedb_migration_dir = os.path.join(migration_dir, "keyvaluedb")
keyvaluedb_dump_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase")
mongo_restore = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongorestore.exe")
slconf_cmd = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NISystemLinkServerConfigCmd.exe")
slconf_cmd_stop = slconf_cmd + " stop-all-services" + " wait"
slconf_cmd_start = slconf_cmd + " start-all-services"

# Import MongoDB dump files
services = ["OpcClient", "TagHistorian"]
for service in services:
    # Get data from service's json config file 
    config_file = os.path.join(program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)

    # Restore mongo database from contents of migration directory
    mongo_dump_file = os.path.join(no_sql_dump_dir, config[service]['Mongo.Database'])
    mongo_restore_cmd = mongo_restore + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --gzip " + mongo_dump_file
    subprocess.run(mongo_restore_cmd)

# Stop SystemLink services to dump Redis DB contents to disk and dump to migration directory
print("Stopping all SystemLink services")
subprocess.run(slconf_cmd_stop)

# Replace the contents of the current Redis DB instance. This will remove previously created tags from the server. 
shutil.copy(keyvaluedb_migration_dir, keyvaluedb_dump_dir)

# Copy OPCUA certificats to data directory
shutil.copytree(opc_cert_migration_dir, sl_data_dir)   

# Restart SystemLink services
print ("Starting all SystemLink services...")
subprocess.run(slconf_cmd_start)
