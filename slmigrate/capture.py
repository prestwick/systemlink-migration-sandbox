from slmigrate import constants, common
import json, subprocess, os, sys, shutil

# def capture_dir_data(service):
#     if not service.directory_migration:
#         return
#     common.check_migration_dir(service.migration_dir)
#     shutil.copytree(service.source_dir, service.migration_dir)  

# def capture_singlefile(service):
#     if  not service.singlefile_migration:
#         return
#     common.check_migration_dir(service.singlefile_migration_dir)
#     os.mkdir(service.singlefile_migration_dir)
#     singlefile_full_path = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", service.singlefile_to_migrate)
#     shutil.copy(singlefile_full_path, service.singlefile_migration_dir)

# def capture_migration(service):
#     print(service.name + " capture migration called")
#     common.migrate_mongo_cmd(service.name, constants.capture_arg)
#     common.stop_sl_service(service)
#     capture_dir_data(service)
#     capture_singlefile(service)
#     common.start_all_sl_services