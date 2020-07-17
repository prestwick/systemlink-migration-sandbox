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

$TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

New-Item -ItemType directory -Path $MigrationDirPath
cd $SlNoSqlPath
.\mongodump.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --out C:\migration\mongo-dump --gzip
.\mongodump.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --out C:\migration\mongo-dump --gzip
cd $SlConfCmdPath
.\NISystemLinkServerConfigCmd.exe stop-all-services
New-Item -ItemType directory -Path $keyValueDbMigrationDir
Copy-Item $keyValueDbDumpSourcePath -Destination $keyValueDbMigrationDir -Verbose
Copy-Item $OpcCertSourcePath -Destination $OpcCertMigrationDirPath -Recurse -Verbose
.\NISystemLinkServerConfigCmd.exe start-all-services