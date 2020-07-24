# Generic migration utility for migrating various data and settings between SystemLink servers. 
# Not all services will be supported. Addtional services will be supported over time. 

import os, json, shutil, subprocess, argparse, sys

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
opcservice = "OpcClient"



# Setup available command line arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument ("--tag", "--tags", "--tagingestion", "--taghistory", help="Migrate tags and tag histories", action="store_true", )
    parser.add_argument ("--opc", "--opcua", "--opcuaclient", help="Migrate OPCUA sessions and certificates", action="store_true")
    return  parser 

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

def migrate_tags():
    print("migrate_tags called")

def migrate_opc():
    print("migrate_opc called")


# Main
if __name__ == "__main__":
    arguments = parse_arguments(sys.argv[1:]).parse_args()
    if arguments.tag:
        migrate_tags()
    if arguments.opc:
        migrate_opc()