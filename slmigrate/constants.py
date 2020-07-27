import os

# Global Constants
migration_dir = os.path.join(os.path.abspath(os.sep), "migration")
no_sql_dump_dir = os.path.join(migration_dir, "mongo-dump")
# program_file_dir = os.environ.get("ProgramW6432")
# program_data_dir = os.environ.get("ProgramData")
# fis_data_source_dir = os.path.join(program_data_dir, "National Instruments", "Skyline", "Data", "FileIngestion")
# fis_data_migration_dir = os.path.join(migration_dir, "FileIngestion")
# mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline", "NoSqlDatabase", "bin", "mongodump.exe")

#Service name strings
tagservice = "TagIngestion"
taghistorian = "TagHistorian"
opcservice = "OpcClient"