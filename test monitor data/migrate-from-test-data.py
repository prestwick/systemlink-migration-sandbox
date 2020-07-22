import os

s = "Hello, world"
print(s)

migration_directory = "C:\migration"
no_sql_dump_dir = os.path.join(migration_directory, "mongo-dump")
program_file_dir = os.environ.get("PROGRAMFILES")
mongo_dump = os.path.join(program_file_dir, "National Instruments", "Shared", "Skyline" "NoSqlDatabase", "bin", "mongodump.exe")
print(mongo_dump)

service= "TestMonitor"
os.system(mongo_dump)