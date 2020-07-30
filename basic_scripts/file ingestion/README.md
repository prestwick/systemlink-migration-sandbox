# Migrate Ingested File 
This example will migrate files uploaded via the File Ingestion service to a new a SystemLink server 

## Python 
### Migrating From an Existing Server
1. Read and understand the [prerequisites](https://github.com/prestwick/systemlink-migration-sandbox/blob/master/README.md#Prerequisites) for this script. 
2. Clone or download this repository
3. Open a cmd or PowerShell window in the directory location of this script
4. Run `py migrate-from-fis.py`
5. Copy the `C:\migration` directory created another SystemLink server.

### Migrating To a New Server
1. Copy the `migration` directory creating by executing the **Migrating From an Existing Server** steps to `C:\` of the new SystemLink server. 
2. Clone or download this repository
3. Open a cmd or PowerShell window in the directory location of this script
4. Run `py migrate-to-fis.py`

## PowerShell
### Migrating From an Existing Server
1. Read and understand the [prerequisites](https://github.com/prestwick/systemlink-migration-sandbox/blob/master/README.md#Prerequisites) for this script. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-from-fis.ps1`
5. Copy the `C:\migration` directory created another SystemLink server. 

### Migrating To a New Server
1. Copy the `migration` directory creating by executing the **Migrating From an Existing Server** steps to `C:\` of the new SystemLink server. 
2. Clone or download this repository
3. Open a PowerShell window in the directory location of this script
4. Run `\.migrate-to-fis.ps1`


