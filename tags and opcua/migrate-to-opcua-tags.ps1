$SlConfCmdPath = "C:\Program Files\National Instruments\Shared\Skyline"
$SlNoSqlPath = "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
$MigrationDirPath = "C:\migration"
$OpcMigrationDirPath = "C:\migration\OpcClient"
$TagHistoryMigrationDirPath = "C:\migration\mongo-dump\nitaghistorian"
$OpcDbMigrationDirPath = "C:\migration\mongo-dump\niopcclient"
$OpcCertMigrationDirPath = "C:\migration\OpcClient"
$KeyValueDbDumpMigrationPath = "C:\migration\keyvaluedb\dump.rdb"
$KeyValueDbPath = "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
$SlDataPath = "C:\ProgramData\National Instruments\Skyline\Data"

$TagHistorianPwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$OpcPwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"

cd $SlNoSqlPath
.\mongorestore.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $TagHistorianPwd --gzip $TagHistoryMigrationDirPath
.\mongorestore.exe --port 27018 --db niopcclient --username niopcclient --password $OpcPwd --gzip $OpcDbMigrationDirPath
cd $SlConfCmdPath
.\NISystemLinkServerConfigCmd.exe stop-all-services
Copy-Item $KeyValueDbDumpMigrationPath -Destination $KeyValueDbPath
Copy-Item $OpcCertMigrationDirPath -Destination $SlDataPath -Recurse -force
.\NISystemLinkServerConfigCmd.exe start-all-services