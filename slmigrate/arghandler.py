import argparse
from slmigrate import constants


# Setup available command line arguments
def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--" + constants.capture_arg, help="capture is used to pull data and settings off SystemLink server", action="store_true", )
    parser.add_argument("--" + constants.restore_arg, help="restore is used to push data and settings to a clean SystemLink server. ", action="store_true", )
    parser.add_argument("--" + constants.tag.arg, "--tags", "--tagingestion", "--taghistory", help="Migrate tags and tag histories", action="store_true", )
    parser.add_argument("--" + constants.opc.arg, "--opcua", "--opcuaclient", help="Migrate OPCUA sessions and certificates", action="store_true")
    parser.add_argument("--" + constants.fis.arg, "--file", "--files", help="Migrate ingested files", action="store_true")
    parser.add_argument("--" + constants.testmonitor.arg, "--test", "--tests", "--testmonitor", help="Migrate Test Monitor Data", action="store_true")
    parser.add_argument("--" + constants.alarmrule.arg, "--alarms", "--alarm", help="Migrate Tag alarm rules", action="store_true")
    return parser


def handle_unallowed_args(arguments):
    if not(arguments.capture) and not(arguments.restore):
        print("Please use --capture or --restore to determine which direction the migration is occuring. ")
    if arguments.capture and arguments.restore:
        print("You cannot use --capture and --restore simultaneously. ")


def determine_migrate_action(arguments):
    services_to_migrate = []
    if arguments.capture:
        action = constants.capture_arg
    elif arguments.restore:
        action = constants.restore_arg
    for arg in vars(arguments):
        if (getattr(arguments, arg) and not ((arg == constants.capture_arg) or (arg == constants.restore_arg))):
            service = getattr(constants, arg)
            services_to_migrate.append((service, action))
    return services_to_migrate
