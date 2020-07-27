# Generic migration utility for migrating various data and settings between SystemLink servers. 
# Not all services will be supported. Addtional services will be supported over time. 

import os, argparse, sys
# from slmigrate.migrate import restore
# from slmigrate.migrate import capture
# import migrate
# from slmigrate.migrate import restore

# This will makes test work, but the script will fail. 
# from slmigrate.migrate import restore
# from slmigrate.migrate import capture

# This will make the app work but test will fail. 
# from migrate import restore
# from migrate import capture

from slmigrate import capture
from slmigrate import restore
from slmigrate import constants

# Setup available command line arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument ("--capture", help="capture is used to pull data and settings off SystemLink server", action="store_true", )
    parser.add_argument ("--restore", help="restore is used to push data and settings to a clean SystemLink server. ", action="store_true", )
    parser.add_argument ("--tag", "--tags", "--tagingestion", "--taghistory", help="Migrate tags and tag histories", action="store_true", )
    parser.add_argument ("--opc", "--opcua", "--opcuaclient", help="Migrate OPCUA sessions and certificates", action="store_true")
    parser.add_argument ("--fis", "--file", "--files", help="Migrate ingested files", action="store_true")
    parser.add_argument ("--test", "--tests", "--testmonitor", help="Migrate Test Monitor Data", action="store_true")
    parser.add_argument ("--alarm", "--alarms", "--alarmrules", help="Migrate Tag alarm rules", action="store_true")
    return  parser 

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# Main
if __name__ == "__main__":
    arguments = parse_arguments(sys.argv[1:]).parse_args()
    if not(arguments.capture) and not(arguments.restore):
        print("Please use --capture or --restore to determine which direction the migration is occuring. ")
    if arguments.capture and arguments.restore:
        print("You cannot use --capture and --restore simultaneously. ")
    if arguments.tag:
        if arguments.capture:
            capture.capture_migration(constants.taghistorian_service)
        if arguments.restore:
            restore.restore_migration(constants.taghistorian_service)
    if arguments.opc:
        if arguments.capture:
            capture.capture_migration(constants.opc_service)
        if arguments.restore:
            restore.restore_migration(constants.opc_service)
    if arguments.fis:
        if arguments.capture:
            capture.capture_migration(constants.file_sevice)
        if arguments.restore:
            restore.restore_migration(constants.file_sevice)
    if arguments.test:
        if arguments.capture:
            capture.capture_migration(constants.testmonitor_service)
        if arguments.restore:
            restore.restore_migration(constants.testmonitor_service)
    if arguments.alarm:
        if arguments.capture:
            capture.capture_migration(constants.tagrule_service)
        if arguments.restore:
            restore.restore_migration(constants.tagrule_service)
            
        