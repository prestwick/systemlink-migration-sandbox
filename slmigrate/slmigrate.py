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



# Setup available command line arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument ("--tag", "--tags", "--tagingestion", "--taghistory", help="Migrate tags and tag histories", action="store_true", )
    parser.add_argument ("--opc", "--opcua", "--opcuaclient", help="Migrate OPCUA sessions and certificates", action="store_true")
    return  parser 

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

def foo():
    print("foo called")

def bar():
    print("bar called")

def bam():
    print("bam called")

def tag():
    print("tag called")


# Main
# def main():
#     parse_arguments(sys.argv[1:])
# parser = parse_arguments(sys.argv[1:])
# arguments = parser.parse_known_args()
# print (arguments[1])
# for argument in arguments:
#     print(argument)
if __name__ == "__main__":
    arguments = parse_arguments(sys.argv[1:]).parse_args()
    if arguments.tag:
        foo()
    if arguments.opc:
        bar()