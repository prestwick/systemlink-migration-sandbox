from slmigrate import constants
from distutils import dir_util
import os
import shutil
import stat


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def determine_migration_dir(service):
    migration_dir = os.path.join(constants.migration_dir, service.name)
    return migration_dir


def migration_dir_exists(dir):
    return os.path.isdir(dir)


def remove_dir(dir):
    if (os.path.isdir(dir)):
        shutil.rmtree(dir, onerror=remove_readonly)


def migrate_singlefile(service, action):
    if not service.singlefile_migration:
        return
    migration_dir = determine_migration_dir(service)
    if action == constants.capture_arg:
        remove_dir(migration_dir)
        os.mkdir(migration_dir)
        singlefile_full_path = os.path.join(constants.program_data_dir, service.singlefile_source_dir, service.singlefile_to_migrate)
        shutil.copy(singlefile_full_path, migration_dir)
    elif action == constants.restore_arg:
        singlefile_full_path = os.path.join(migration_dir, service.singlefile_to_migrate)
        if not os.path.isfile(singlefile_full_path):
            raise FileNotFoundError
        shutil.copy(singlefile_full_path, service.singlefile_source_dir)


def migrate_dir(service, action):
    if not service.directory_migration:
        return
    migration_dir = determine_migration_dir(service)
    if action == constants.capture_arg:
        remove_dir(migration_dir)
        shutil.copytree(service.source_dir, migration_dir)
    elif action == constants.restore_arg:
        if not os.path.isdir(migration_dir):
            raise FileNotFoundError
        remove_dir(service.source_dir)
        dir_util.copy_tree(migration_dir, service.source_dir)
