# migrate-from-opcua-tags.ps1

# This example will generate a migration directory container all tags, tag histories, OPCUA sessions, and OPCUA certificates on the SystemLink Server.  
# This script will migrate all tags, not just those created by OPCUA session monitors. 

# Set variables for various paths used during migration
$SlConfCmdDir = "C:\Program Files\National Instruments\Shared\Skyline"
$NoSqlDir = "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
$MigrationDir = "C:\migration"
$OpcMigrationDir = "C:\migration\OpcClient"
$NoSqlDumpDir = "C:\migration\mongo-dump"
$TagHistorianMigrationDir = "C:\migration\mongo-dump\nitaghistorian"
$OpcCertSourceDir  = "C:\ProgramData\National Instruments\Skyline\Data\OpcClient"
$OpcDbMigrationDir = "C:\migration\mongo-dump\niopcclient"
$OpccertMigrationDir = "C:\migration\OpcClient"
$keyValueDbMigrationDir = "C:\migration\keyvaluedb"
$KeyValueDbMigrationDump = "C:\migration\keyvaluedb\dump.rdb"
$KeyValueDbDumpSource = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase\dump.rdb"
$KeyValueDbDir = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
$SlDataDir = "C:\ProgramData\National Instruments\Skyline\Data"

#Prompt user for database passwords
$TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

#Create Migration Directory
New-Item -ItemType directory -Path $MigrationDir

# Produce MongoDB dump files 
cd $NoSqlDir
.\mongodump.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --out $NoSqlDumpDir --gzip
.\mongodump.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --out C:\migration\mongo-dump --gzip

# Stop SystemLink services to dump Redis DB contents to disk and dump to migration directory
cd $SlConfCmdDir
Write-Host "Stopping all SystemLink services..."
.\NISystemLinkServerConfigCmd.exe stop-all-services
New-Item -ItemType directory -Path $keyValueDbMigrationDir
Copy-Item $KeyValueDbDumpSource -Destination $keyValueDbMigrationDir -Verbose

# Copy OPCUA certificats to migration directory
Copy-Item $OpcCertSourceDir -Destination $OpccertMigrationDir -Recurse -Verbose

# Restart SystemLink services
Write-Host "Starting all SystemLink services..."
.\NISystemLinkServerConfigCmd.exe start-all-services