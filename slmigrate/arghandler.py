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
    parser.add_argument("--" + constants.asset.arg, "--assets", help="Migrate asset utilitization and calibration data", action="store_true")
    parser.add_argument("--" + constants.alarmrule.arg, "--alarms", "--alarm", help="Migrate Tag alarm rules", action="store_true")
    parser.add_argument("--" + constants.migration_arg, "--directory", "--folder", help="Specify the directory used for migrated data", action="store", default=constants.migration_dir)
    
    return parser


def handle_unallowed_args(arguments):
    if not(arguments.capture) and not(arguments.restore):
        print("Please use --capture or --restore to determine which direction the migration is occuring. ")
        exit()
    if arguments.capture and arguments.restore:
        print("You cannot use --capture and --restore simultaneously. ")
        exit()


def determine_migrate_action(arguments):
    services_to_migrate = []
    if arguments.capture:
        action = constants.capture_arg
    elif arguments.restore:
        action = constants.restore_arg
    for arg in vars(arguments):
        if (getattr(arguments, arg) and not ((arg == constants.capture_arg) or (arg == constants.restore_arg) or (arg == constants.migration_arg))):
            service = getattr(constants, arg)
            services_to_migrate.append((service, action))
    return services_to_migrate


def determine_migration_dir(arguments):
    constants.migration_dir = getattr(arguments, constants.migration_arg)
