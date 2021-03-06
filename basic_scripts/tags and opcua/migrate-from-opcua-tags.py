# migrate-from-opcua-tags.py

# This example will generate a migration directory container all tags, tag histories, OPCUA sessions, and OPCUA certificates on the SystemLink Server.  
# This script will migrate all tags, not just those created by OPCUA session monitors. 

import os, subprocess, json, shutil

# Set variables for various paths used during migration
migration_dir = "C:\migration"
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")
opc_migration_dir= os.path.join(migration_dir, "OpcClient")
opc_cert_source_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "OpcClient")
opc_cert_migration_dir = os.path.join(migration_dir, "OpcClient")
keyvaluedb_migration_dir = os.path.join(migration_dir, "keyvaluedb")
keyvaluedb_dump_source = os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", "dump.rdb")
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")
slconf_cmd = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NISystemLinkServerConfigCmd.exe")
slconf_cmd_stop = slconf_cmd + " stop-all-services" + " wait"
slconf_cmd_start = slconf_cmd + " start-all-services"

#FOR LOOP HERE
services = ["OpcClient", "TagHistorian"]
for service in services:
    # Get data from service's json config file 
    config_file = os.path.join(program_data_dir, "National Instruments", "Skyline", "Config", service+".json")
    with open(config_file, encoding='utf-8-sig') as json_file:
        config = json.load(json_file)

    # Dump mongo database to migration directory
    mongo_dump_cmd = mongo_dump + " --port " + str(config[service]['Mongo.Port']) + " --db " + config[service]['Mongo.Database'] + " --username " + config[service]['Mongo.User'] + " --password " + config[service]['Mongo.Password'] + " --out " + no_sql_dump_dir + " --gzip"
    subprocess.run(mongo_dump_cmd)

# Stop SystemLink services to dump Redis DB contents to disk and dump to migration directory

print("Stopping all SystemLink services")
subprocess.run(slconf_cmd_stop)

# Stop SystemLink services to dump Redis DB contents to disk and dump to migration directory
os.mkdir(keyvaluedb_migration_dir)
shutil.copy(keyvaluedb_dump_source, keyvaluedb_migration_dir)

# Copy OPCUA certificats to migration directory
# os.mkdir(opc_cert_migration_dir)
# opc_cert_files = os.listdir(opc_cert_source_dir)
shutil.copytree(opc_cert_source_dir, opc_cert_migration_dir)   



# migration_files = os.listdir(fis_data_source_dir)
# for file_name in migration_files:
#     full_file_path = os.path.join(fis_data_source_dir, file_name)
#     if os.path.isfile(full_file_path):
#         shutil.copy(full_file_path, fis_data_migration_dir)

# Restart SystemLink services
print ("Starting all SystemLink services...")
subprocess.run(slconf_cmd_start)
