# systemlink-migration-sandbox
A place for example PowerShell scripts used to migrate data and setting between SystemLink servers. We encourage migration to servers with a fresh install of SystemLink that contains no production data. 


## Prerequisites 
- These scripts assume migration from a SystemLink 2020R1 (20.0) to another SystemLink 2020R1 server
- These scripts assume a single-box SystemLink installation. 
- These scripts are designed to un on the same machines as the SystemLink installation. They do not support remote migration. 
- PowerShell must be run as an administrator. 
- The Powershell `Set-ExecutionPolicy` cmdlet may have to be modified to run Powershell scripts. See [SetExecution-Policy](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7]) for more details on modifying this setting. 

## Basic Migration Pattern
These scripts use `mongodump` and `mongorestore` commands, and file copies to orchestrate migration of various data and settings in SystemLink. This pattern can be extended to cover additional aspects of SystemLink. Only the scripts within this repository has been tested by NI. 

## Migrate OPCUA, Tags, and Tag History
[tags and opcua](https://github.com/prestwick/systemlink-migration-sandbox/tree/master/tags%20and%20opcua)
This example will migrate all tags, tag histories, OPCUA sessions and certificates. 