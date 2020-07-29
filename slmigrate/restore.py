from slmigrate import constants, common
import json, subprocess, os, sys, shutil
from distutils import dir_util

# def restore_dir_data(service):
#     if not service.directory_migration:
#         return
#     dir_util.copy_tree(service.migration_dir, service.source_dir)

# def restore_singlefile(service):
#     if not service.singlefile_migration:
#         return
#     singlefile_full_path = os.path.join(service.singlefile_migration_dir, service.singlefile_to_migrate) 
#     shutil.copy(singlefile_full_path, service.singlefile_source_dir)

# def restore_migration(service):
#     print(service.name + " restore migration called")
#     common.migrate_mongo_cmd(service.name, constants.restore_arg)
#     common.stop_sl_service(service)
#     restore_dir_data(service)
#     restore_singlefile(service)
#     common.start_all_sl_services(service)