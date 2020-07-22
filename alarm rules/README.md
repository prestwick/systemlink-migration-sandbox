# Migrate Tag Alarm Rule
This example will migrate tag alarms rules. This includes the default tag alarm rules created when SystemLink is installed. 
Note this may lead to duplicate rules in the new server

## Migrating From an Existing Server
1. Read and understand the [prerequisites](https://github.com/prestwick/systemlink-migration-sandbox/blob/master/README.md#Prerequisites) for this script. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-from-alarms-rules.ps1`
5. Copy the `C:\migration` directory created another SystemLink server. 

## Migrating To a New Server
1. Copy the `migration` directory creating by executing the **Migrating From an Existing Server** steps to `C:\` of the new SystemLink server. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-to-alarms-rules.ps1`


