$tag_historian_pwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$opc_pwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"
New-Item -ItemType directory -Path C:\migration
cd "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
.\mongodump.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $tag_historian_pwd --out C:\migration\mongo-dump --gzip
.\mongodump.exe --port 27018 --db niopcclient --username niopcclient --password $opc_pwd --out C:\migration\mongo-dump --gzip
cd "C:\Program Files\National Instruments\Shared\Skyline"
.\NISystemLinkServerConfigCmd.exe stop-all-services
Copy-Item "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase\dump.rdb" -Destination "C:\migration\keyvaluedb" -Verbose
Copy-Item "C:\ProgramData\National Instruments\Skyline\Data\OpcClient" -Destination "C:\migration\opc" -Recurse -Verbose
cd "C:\Program Files\National Instruments\Shared\Skyline"
.\NISystemLinkServerConfigCmd.exe start-all-services