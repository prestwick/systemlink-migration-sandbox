# Generic migration utility for migrating various data and settings between SystemLink servers. 
# Not all services will be supported. Addtional services will be supported over time. 

import os, argparse, sys
from slmigrate import capture
from slmigrate import restore
from slmigrate import constants

# Setup available command line arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument ("--" + constants.capture_arg, help="capture is used to pull data and settings off SystemLink server", action="store_true", )
    parser.add_argument ("--" + constants.restore_arg, help="restore is used to push data and settings to a clean SystemLink server. ", action="store_true", )
    parser.add_argument ("--" + constants.tag.arg, "--tags", "--tagingestion", "--taghistory", help="Migrate tags and tag histories", action="store_true", )
    parser.add_argument ("--" + constants.opc.arg, "--opcua", "--opcuaclient", help="Migrate OPCUA sessions and certificates", action="store_true")
    parser.add_argument ("--" + constants.fis.arg, "--file", "--files", help="Migrate ingested files", action="store_true")
    parser.add_argument ("--" + constants.testmonitor.arg, "--test", "--tests", "--testmonitor", help="Migrate Test Monitor Data", action="store_true")
    parser.add_argument ("--" + constants.alarmrule.arg, "--alarms", "--alarm", help="Migrate Tag alarm rules", action="store_true")
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
    if arguments.capture:
        for arg in vars(arguments):
            if (getattr(arguments, arg) and arg != constants.capture_arg):
                service_to_migrate = getattr(constants, arg)
                print (service_to_migrate)
                capture.capture_migration(service_to_migrate)
    if arguments.restore:
        for arg in vars(arguments):
            if (getattr(arguments, arg) and arg != constants.restore_arg):
                service_to_migrate = getattr(constants, arg)
                print (service_to_migrate)
                restore.restore_migration(service_to_migrate)
                