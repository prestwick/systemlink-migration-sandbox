import os

#Service name strings
tag_service = "TagIngestion"
taghistorian_service = "TagHistorian"
opc_service = "OpcClient"
file_sevice = "FileIngestion"
testmonitor_service = "TestMonitor"
tagrule_service = "TagRuleEngine"

# Global Constants
migration_dir = os.path.join(os.path.abspath(os.sep), "migration")
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")

fis_data_source_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "FileIngestion")
fis_data_migration_dir = os.path.join(migration_dir, "FileIngestion")

opc_migration_dir= os.path.join(migration_dir, "OpcClient")
opc_cert_source_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "OpcClient")
opc_cert_migration_dir = os.path.join(migration_dir, "OpcClient")

keyvaluedb_migration_dir = os.path.join(migration_dir, "keyvaluedb")
keyvaluedb_dump_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase")
keyvaluedb_dump = os.path.join(keyvaluedb_migration_dir, "dump.rdb")
keyvaluedb_dump_source = os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", "dump.rdb")

mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")
slconf_cmd = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NISystemLinkServerConfigCmd.exe")
slconf_cmd_stop = slconf_cmd + " stop-all-services" + " wait"
slconf_cmd_start = slconf_cmd + " start-all-services"
slconf_cmd_stop_tag = slconf_cmd + " stop-service " + tag_service
slconf_cmd_start_tag = slconf_cmd + " start-service " + tag_service

