from slmigrate import constants
from distutils import dir_util
import os
import shutil


def check_migration_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir)


def migrate_singlefile(service, action):
    if not service.singlefile_migration:
        return
    if action == constants.capture_arg:
        check_migration_dir(service.singlefile_migration_dir)
        os.mkdir(service.singlefile_migration_dir)
        singlefile_full_path = os.path.join(constants.program_data_dir, "National Instruments", "Skyline", "KeyValueDatabase", service.singlefile_to_migrate)
        shutil.copy(singlefile_full_path, service.singlefile_migration_dir)
    elif action == constants.restore_arg:
        singlefile_full_path = os.path.join(service.singlefile_migration_dir, service.singlefile_to_migrate)
        shutil.copy(singlefile_full_path, service.singlefile_source_dir)


def migrate_dir(service, action):
    if not service.directory_migration:
        return
    if action == constants.capture_arg:
        check_migration_dir(service.migration_dir)
        shutil.copytree(service.source_dir, service.migration_dir)
    elif action == constants.restore_arg:
        dir_util.copy_tree(service.migration_dir, service.source_dir)
