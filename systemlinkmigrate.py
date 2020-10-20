# Generic migration utility for migrating various data and settings between SystemLink servers.
# Not all services will be supported. Addtional services will be supported over time.

import sys
from slmigrate import mongohandler, filehandler, arghandler, servicemgrhandler, constants

# Main
if __name__ == "__main__":
    arguments = arghandler.parse_arguments().parse_args()
    arghandler.determine_migration_dir(arguments)
    arghandler.determine_source_db(arguments)
    servicemgrhandler.stop_all_sl_services()
    mongo_proc = mongohandler.start_mongo(constants.mongod_exe, constants.mongo_config)
    services_to_migrate = arghandler.determine_migrate_action(arguments)
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
