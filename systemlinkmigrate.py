# Generic migration utility for migrating various data and settings between SystemLink servers.
# Not all services will be supported. Addtional services will be supported over time.

import sys
from slmigrate import mongohandler, filehandler, arghandler, servicemgrhandler

# Main
if __name__ == "__main__":
    arguments = arghandler.parse_arguments(sys.argv[1:]).parse_args()
    arghandler.handle_unallowed_args(arguments)
    servicemgrhandler.stop_all_sl_services()
    mongo_proc = mongohandler.start_mongo()
    service_to_migrate = arghandler.determine_migrate_action(arguments)
    service = service_to_migrate[0]
    action = service_to_migrate[1]
    print(service.name + " " + action + " migration called")
    mongohandler.migrate_mongo_cmd(service, action)
    filehandler.migrate_dir(service, action)
    filehandler.migrate_singlefile(service, action)
    mongohandler.stop_mongo(mongo_proc)
    servicemgrhandler.start_all_sl_services()
