# migrate-to-opcua-tags.ps1

# This example will migrate all tags, tag histories, OPCUA session, and OPCUA certificates generated from running migrate-from-opcua-tags.ps1 to another SystemLink Server
# This script will migrate all tags, not just those created by OPCUA session monitors. 

# Set variables for various paths used during migration
$MigrationDir = "C:\migration"
# $OpcMigrationDir = Join-Path $MigrationDir OpcClient
$NoSqlDumpDir = Join-Path $MigrationDir mongo-dump
# $OpcCertSourceDir = Join-Path $env:ProgramData "National Instruments" Skyline Data OpcClient
$OpcCertMigrationDir = Join-Path $MigrationDir OpcClient 
$keyValueDbMigrationDir = Join-Path $MigrationDir keyvaluedb
# $KeyValueDbDumpSource = Join-Path $env:ProgramData "National Instruments" Skyline KeyValueDatabase dump.rdb
$MongoRestore = Join-Path $env:ProgramFiles "National Instruments" Shared Skyline NoSqlDatabase bin mongorestore.exe
$SlConfCmd = Join-Path $env:ProgramFiles "National Instruments" Shared Skyline NISystemLinkServerConfigCmd.exe




# $SlConfCmdDir = "C:\Program Files\National Instruments\Shared\Skyline"
# $NoSqlDir = "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
# $MigrationDir = "C:\migration"
# $OpcMigrationDir = "C:\migration\OpcClient"
# $TagHistorianMigrationDir = "C:\migration\mongo-dump\nitaghistorian"
$TagHistorianMigrationDir = Join-Path $NoSqlDumpDir nitaghistorian

# $OpcDbMigrationDir = "C:\migration\mongo-dump\niopcclient"
$OpcDbMigrationDir = Join-Path $NoSqlDumpDir niopcclient
# $OpccertMigrationDir = "C:\migration\OpcClient"
# $KeyValueDbMigrationDump = "C:\migration\keyvaluedb\dump.rdb"
$KeyValueDbMigrationDump = $KeyValueDbMigrationDir dump.rdb

# $KeyValueDbDir = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
$KeyValueDbDir = Join-Path $env:ProgramData "National Instruments" Skyline KeyValueDatabase

# $SlDataDir = "C:\ProgramData\National Instruments\Skyline\Data"
$SlDataDir = Join-Path $env:ProgramData "National Instruments Skyline Data"

#Prompt user for database passwords
# $TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
# $OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

# Import MongoDB dump files 
# cd $NoSqlDir
# .\mongorestore.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --gzip $TagHistorianMigrationDir
# .\mongorestore.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --gzip $OpcDbMigrationDir
$Service = "OpcClient"
For ($i=0; $i -lt 2; $i++) {
    $ConfigFile = Join-Path $env:ProgramData "National Instruments" Skyline Config "$Service.json"
    $Config = (Get-Content $ConfigFile | ConvertFrom-Json).$Service

    . $MongoRestore --port $Config."Mongo.Port" --db $Config."Mongo.Database" --username $Config."Mongo.User" --password $Config."Mongo.Password" --gzip $OpcDbMigrationDir
    $Service = "TagHistorian"
}






# Replace the contents of the current Redis DB instance. This will remove previously created tags from the server. 
# cd $SlConfCmdDir
Write-Host "Stopping all SystemLink services..."
# .\NISystemLinkServerConfigCmd.exe stop-all-services
. $SlConfCmd stop-all-services
Copy-Item $KeyValueDbMigrationDump -Destination $KeyValueDbDir

# Copy OPCUA certificates to new server
Copy-Item $OpcCertMigrationDir -Destination $SlDataDir -Recurse -force

# Restart SystemLink services
Write-Host "Starting all SystemLink services..."
# .\NISystemLinkServerConfigCmd.exe start-all-services
. $SlConfCmd start-all-services