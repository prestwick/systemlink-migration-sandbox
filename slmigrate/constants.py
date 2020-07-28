import os

# Global Path Constants
migration_dir = os.path.join(os.path.abspath(os.sep), "migration")
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
program_file_dir = os.environ.get("ProgramW6432")
program_data_dir = os.environ.get("ProgramData")

# Variables for calling EXEs
slconf_cmd = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NISystemLinkServerConfigCmd.exe")
slconf_cmd_stop_all = slconf_cmd + " stop-all-services" + " wait"
slconf_cmd_start_all = slconf_cmd + " start-all-services"
slconf_cmd_stop_service = slconf_cmd + " stop-service "
slconf_cmd_start_service = slconf_cmd + " start-service "
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")

# Service Dictionaries
tag = {
    'arg': 'tag',
    'service': "TagHistorian",
    'directory_migration': False,
    'singlefile_migration': True,
    'require_service_restart': True,
    'singlefile_migration_dir': os.path.join(migration_dir, "keyvaluedb"),
    'singlefile_source_dir': os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase"),
    'singlefile_to_migrate': os.path.join(program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", "dump.rdb")
}

opc = {
    'arg': 'opc',
    'service': "OpcClient",
    'directory_migration': True,
    'singlefile_migration': False,
    'require_service_restart': False,
    'migration_dir': os.path.join(migration_dir, "OpcClient"),
    'source_dir': os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "OpcClient")
}

fis = {
    'arg': 'fis',
    'service': "FileIngestion",
    'directory_migration': True,
    'singlefile_migration': False,
    'require_service_restart': False,
    'migration_dir': os.path.join(migration_dir, "FileIngestion"),
    'source_dir': os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "FileIngestion")   
}

testmonitor = {
    'arg': 'testmonitor',
    'service': "TestMonitor",
    'directory_migration': False,
    'singlefile_migration': False,
    'require_service_restart': False,
}

alarmrule = {
    'arg': 'alarmrule',
    'service': "TagRuleEngine",
    'directory_migration': False,
    'singlefile_migration': False,
    'require_service_restart': False,
}

# Capture and Restore argument constants
capture_arg = 'capture'
restore_arg = 'restore'

