# Generic migration utility for migrating various data and settings between SystemLink servers.
# Not all services will be supported. Addtional services will be supported over time.

import sys
from slmigrate import mongohandler, filehandler, arghandler, servicemgrhandler, constants

# Main
if __name__ == "__main__":
    argparser = arghandler.parse_arguments()
    arguments = argparser.parse_args()
    arghandler.determine_migration_dir(arguments)
    if arguments.action == constants.restore_arg and not filehandler.migration_dir_exists(constants.migration_dir):
        argparser.error("Migration directory does not exist for restore")
    arghandler.determine_source_db(arguments)
    servicemgrhandler.stop_all_sl_services()
    mongo_proc = mongohandler.start_mongo(constants.mongod_exe, constants.mongo_config)
    services_to_migrate = arghandler.determine_migrate_action(arguments)
    for service_to_migrate in services_to_migrate:
        service = service_to_migrate[0]
        action = service_to_migrate[1]
        print(service.name + " " + action + " migration called")
        config = mongohandler.get_service_config(service)
        try:
            mongohandler.migrate_mongo_cmd(service, action, config)
            filehandler.migrate_dir(service, action)
            filehandler.migrate_singlefile(service, action)
        except FileNotFoundError:
            argparser.error("Service migration files do not exist for " + service.name)
    mongohandler.stop_mongo(mongo_proc)
    servicemgrhandler.start_all_sl_services()
