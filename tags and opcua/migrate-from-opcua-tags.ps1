# migrate-from-opcua-tags.ps1

# This example will generate a migration directory container all tags, tag histories, OPCUA sessions, and OPCUA certificates on the SystemLink Server.  
# This script will migrate all tags, not just those created by OPCUA session monitors. 

# Set variables for various paths used during migration
$SlConfCmdPath = "C:\Program Files\National Instruments\Shared\Skyline"
$SlNoSqlPath = "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
$MigrationDirPath = "C:\migration"
$OpcMigrationDirPath = "C:\migration\OpcClient"
$TagHistoryMigrationDirPath = "C:\migration\mongo-dump\nitaghistorian"
$OpcCertSourcePath  = "C:\ProgramData\National Instruments\Skyline\Data\OpcClient"
$OpcDbMigrationDirPath = "C:\migration\mongo-dump\niopcclient"
$OpcCertMigrationDirPath = "C:\migration\OpcClient"
$keyValueDbMigrationDir = "C:\migration\keyvaluedb"
$KeyValueDbDumpMigrationPath = "C:\migration\keyvaluedb\dump.rdb"
$keyValueDbDumpSourcePath = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase\dump.rdb"
$KeyValueDbPath = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
$SlDataPath = "C:\ProgramData\National Instruments\Skyline\Data"

#Prompt user for database passwords
$TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

#Create Migration Directory
New-Item -ItemType directory -Path $MigrationDirPath

# Produce MongoDB dump files 
cd $SlNoSqlPath
.\mongodump.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --out C:\migration\mongo-dump --gzip
.\mongodump.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --out C:\migration\mongo-dump --gzip

# Stop SystemLink services to dump Redis DB contents to disk and dump to migration directory
cd $SlConfCmdPath
.\NISystemLinkServerConfigCmd.exe stop-all-services
New-Item -ItemType directory -Path $keyValueDbMigrationDir
Copy-Item $keyValueDbDumpSourcePath -Destination $keyValueDbMigrationDir -Verbose

# Copy OPCUA certificats to migration directory
Copy-Item $OpcCertSourcePath -Destination $OpcCertMigrationDirPath -Recurse -Verbose

# Restart SystemLink services. 
.\NISystemLinkServerConfigCmd.exe start-all-services