# Generic migration utility for migrating various data and settings between SystemLink servers. 
# Not all services will be supported. Addtional services will be supported over time. 

import os, argparse, sys
from slmigrate import capture, restore, constants, mongohandler, filehandler, arghandler, servicemgrhandler

# Main
if __name__ == "__main__":
    arguments = arghandler.parse_arguments(sys.argv[1:]).parse_args()
    arghandler.handle_unallowed_args(arguments)
    service_to_migrate = arghandler.determine_migrate_action(arguments)
    service = service_to_migrate[0]
    action = service_to_migrate[1]
    print(service.name + " " + action + " migration called")
    mongohandler.migrate_mongo_cmd(service, action)
    servicemgrhandler.stop_sl_service(service)
    filehandler.migrate_dir(service, action)
    filehandler.migrate_singlefile(service, action)
    servicemgrhandler.start_all_sl_services