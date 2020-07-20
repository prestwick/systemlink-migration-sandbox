# migrate-to-opcua-tags.ps1

# This example will migrate all tags, tag histories, OPCUA session, and OPCUA certificates generated from running migrate-from-opcua-tags.ps1 to another SystemLink Server
# This script will migrate all tags, not just those created by OPCUA session monitors. 

# Set variables for various paths used during migration
$SlConfCmdDir = "C:\Program Files\National Instruments\Shared\Skyline"
$NoSqlDir = "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
$MigrationDir = "C:\migration"
$OpcMigrationDir = "C:\migration\OpcClient"
$TagHistorianMigrationDir = "C:\migration\mongo-dump\nitaghistorian"
$OpcDbMigrationDir = "C:\migration\mongo-dump\niopcclient"
$OpccertMigrationDir = "C:\migration\OpcClient"
$KeyValueDbMigrationDump = "C:\migration\keyvaluedb\dump.rdb"
$KeyValueDbDir = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
$SlDataDir = "C:\ProgramData\National Instruments\Skyline\Data"

#Prompt user for database passwords
$TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

# Import MongoDB dump files 
cd $NoSqlDir
.\mongorestore.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --gzip $TagHistorianMigrationDir
.\mongorestore.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --gzip $OpcDbMigrationDir

# Replace the contents of the current Redis DB instance. This will remove previously created tags from the server. 
cd $SlConfCmdDir
Write-Host "Stopping all SystemLink services..."
.\NISystemLinkServerConfigCmd.exe stop-all-services
Copy-Item $KeyValueDbMigrationDump -Destination $KeyValueDbDir

# Copy OPCUA certificates to new server
Copy-Item $OpccertMigrationDir -Destination $SlDataDir -Recurse -force

# Restart SystemLink services
Write-Host "Starting all SystemLink services..."
.\NISystemLinkServerConfigCmd.exe start-all-services