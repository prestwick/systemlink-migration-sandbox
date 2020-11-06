# Generic migration utility for migrating various data and settings between SystemLink servers.
# Not all services will be supported. Addtional services will be supported over time.

import sys, os
from slmigrate import mongohandler, filehandler, arghandler, servicemgrhandler, constants


# Main
def main():
    argparser = arghandler.parse_arguments()
    arguments = argparser.parse_args()
    arghandler.determine_migration_dir(arguments)
    services_to_migrate = arghandler.determine_migrate_action(arguments)
    if arguments.action == constants.restore_arg and not filehandler.migration_dir_exists(constants.migration_dir):
        argparser.error(constants.migration_dir + " does not exist")
    for service_to_migrate in services_to_migrate:
        service = service_to_migrate[0]
        action = service_to_migrate[1]
        if action == constants.restore_arg:
            if not filehandler.service_restore_singlefile_exists(service):
                argparser.error(service.name + ": " + os.path.join(filehandler.determine_migration_dir(service), service.singlefile_to_migrate) + " does not exist")
            if not filehandler.service_restore_dir_exists(service):
                argparser.error(service.name + ": " + filehandler.determine_migration_dir(service) + " does not exist")
    arghandler.determine_source_db(arguments)
    servicemgrhandler.stop_all_sl_services()
    mongo_proc = mongohandler.start_mongo(constants.mongod_exe, constants.mongo_config)
    for service_to_migrate in services_to_migrate:
        service = service_to_migrate[0]
        action = service_to_migrate[1]
        print(service.name + " " + action + " migration called")
        config = mongohandler.get_service_config(service)
        mongohandler.migrate_mongo_cmd(service, action, config)
        filehandler.migrate_dir(service, action)
        filehandler.migrate_singlefile(service, action)
    mongohandler.stop_mongo(mongo_proc)
    servicemgrhandler.start_all_sl_services()


if __name__ == "__main__":
    main()   