# Migrate OPCUA, Tags, and Tag History
This example will migrate all tags, tag histories, OPCUA sessions, and OPCUA certificates. This script will migrate all tags, not just those created by OPCUA session monitors. 

## Python 
### Migrating From an Existing Server
1. Read and understand the [prerequisites](https://github.com/prestwick/systemlink-migration-sandbox/blob/master/README.md#Prerequisites) for this script. 
2. Clone or download this repository
3. Open a cmd or PowerShell window in the directory location of this script
4. Run `py migrate-from-opcua-tags.py`
5. Copy the `C:\migration` directory created another SystemLink server.

### Migrating To a New Server
1. Copy the `migration` directory creating by executing the **Migrating From an Existing Server** steps to `C:\` of the new SystemLink server. 
2. Clone or download this repository
3. Open a cmd or PowerShell window in the directory location of this script
4. Run `py migrate-to-opcua-tags.py`

## PowerShell
### Migrating From an Existing Server
1. Read and understand the [prerequisites](https://github.com/prestwick/systemlink-migration-sandbox/blob/master/README.md#Prerequisites) for this script. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-from-opcua-tags.ps1`
5. Copy the `C:\migration` directory created another SystemLink server. 

### Migrating To a New Server
1. Copy the `migration` directory creating by executing the **Migrating From an Existing Server** steps to `C:\` of the new SystemLink server. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-to-opcua-tags.ps1`
5. If SystemLink service manager did not automatically start, open **NI SystemLink Server Configuration** and restart **NI SystemLink Service Manager**. 
    - You can also restart Service Manager from the command line by open a command window as an administrator at `C:\Program Files\National Instruments\Shared\Skyline` and running the command `.\NISystemLinkServerConfigCmd.exe start-all-services`. 