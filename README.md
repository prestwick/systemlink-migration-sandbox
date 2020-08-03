# systemlink-migration-sandbox
A place for example PowerShell scripts used to migrate data and setting between SystemLink servers. We encourage migration to servers with a fresh install of SystemLink that contains no production data. 

# Migrating with systemlinkmigrate.py

## Prerequisites 
### SystemLink
- These scripts assume migration from a SystemLink 2020R1 (20.0) to another SystemLink 2020R1 server
- These scripts assume the SystemLink server you are migrating TO is a fresh install with no existing data or systems. 
- These scripts assume a single-box SystemLink installation. 
- These scripts are designed to un on the same machines as the SystemLink installation. They do not support remote migration.

### Python
- These scripts require >=Python3 to run. Installers can be found at [python.org](https://www.python.org/downloads/)
- The documentation in this repo assumes Python has been added to your **PATH**. 
- Depending on the setup of your environment you may invoke python with `python`, `python3`, or `py`. Documentation in this repo use `py`. 

## Running systemlinkmigrate.py
### Basic usage

```bash
py systemlinkmigrate.py --capture --tags
```
Running `systemlinkmigrate.py` with the above arguments will capture tag and tag history and store this data in `C:\migration`. 

```bash
py systemlinkmigrate.py --restore --tags
```

Running `systemlinkmigrate.py` with the above arguments will restore tag and tag history data from the directory `C:\migration`

### Capture and Restore
The `--capture` and `--restore` arguments determine the directionality of the migration. The `--capture` argument is used when migrating data FROM an existing SystemLink server. The `--restore` argument is used when migrating data TO a new SystemLink server. At least one of these arguments must be specified and both arguments cannot be used simultaneously. 

### Specifying services to migrate
To migrate the data associated with a SystemLink service you must specify the service as an argument. Multiple services may be captured or restored by providing multiple arguments; e.g.

```bash
py systemlinkmigrate.py --capture --tags --opc
```

#### Supported Services
The following services can be migrated with this utility:

- Tag Ingestion and Tag History: `--tag`
- Tag Alarm Rules: `--alarm`
- OPCUA Client: `--opc`
- File Ingestion: `--file`
- Test Monitor: `--test`

## Specifying a Migration Directory
By default this tool will migrate data into the directory `C:\migrate`. During *capture* this directory is created. During *restore* this directory is expected to be present. The `--dir` argument allows for other directories and locations to be specified. For example:
```bash
py systemlinkmigrate.py --capture --tag --dir="C:\migrate_8-3-2020
````
These arguments will capture tag and tag history data and store them in the directory `C:\migrate_8-3-2020`