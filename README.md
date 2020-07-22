# systemlink-migration-sandbox
A place for example PowerShell scripts used to migrate data and setting between SystemLink servers. We encourage migration to servers with a fresh install of SystemLink that contains no production data. 

## Prerequisites 
### SystemLink
- These scripts assume migration from a SystemLink 2020R1 (20.0) to another SystemLink 2020R1 server
- These scripts assume a single-box SystemLink installation. 
- These scripts are designed to un on the same machines as the SystemLink installation. They do not support remote migration. 

### Migrating  with Python
- These scripts require >=Python3 to run. Installers can be found at [python.org](https://www.python.org/downloads/)
- The documentation in this repo assumes Python has been added to your PATH variable. 
- Depending on the setup of your environment you may invoke python with `python`, `python3`, or `py`. Documentation in this repo use `py`. 

### Migrating with PowerShell
- These scripts require PowerShell 7 to run. Installers can be found in the [Powershell Github repo](https://github.com/PowerShell/PowerShell/releases). 
- PowerShell must be run as an administrator. 
- The Powershell `Set-ExecutionPolicy` cmdlet may have to be modified to run Powershell scripts. See [SetExecution-Policy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7]) for more details on modifying this setting. 

## Basic Migration Pattern
These scripts use `mongodump` and `mongorestore` commands, and file copies to orchestrate migration of various data and settings in SystemLink. This pattern can be extended to cover additional aspects of SystemLink. The current set of scripts demonstrate the migration of subsets of the overall data ingested by SystemLink, but each script can be used sequentially to dump more data into the `migration` directory. 

## Migrate OPCUA, Tags, and Tag History
[tags and opcua](https://github.com/prestwick/systemlink-migration-sandbox/tree/master/tags%20and%20opcua)

This example will migrate all tags, tag histories, OPCUA sessions and certificates. 

## Migrate Test Results and Test Steps
[test monitor data](https://github.com/prestwick/systemlink-migration-sandbox/tree/master/test%20monitor%20data)

This example will migrate test results and test step data. 

# Migrate Tag Alarm Rule
[alarm rules](https://github.com/prestwick/systemlink-migration-sandbox/tree/master/alarm%20rules)

This example will migrate tag alarms rules. This includes the default tag alarm rules created when SystemLink is installed. 

# Migrate Ingested File 
[file ingestion](https://github.com/prestwick/systemlink-migration-sandbox/tree/master/file%20ingestion)

This example will migrate files uploaded via the File Ingestion service to a new a SystemLink server 