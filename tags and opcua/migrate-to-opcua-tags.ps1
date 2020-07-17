$tag_historian_pwd = Read-Host "Enter the mongo password for the tag historian found at C:\ProgramData\National Instruments\Skyline\Config\Taghistorian.json" 
$opc_pwd = Read-Host "Enter the mongo password for OPCUA client found at C:\ProgramData\National Instruments\Skyline\Config\OpcClient.json"
cd "C:\Program Files\National Instruments\Shared\Skyline\NoSqlDatabase\bin"
.\mongorestore.exe --port 27018 --db nitaghistorian --username nitaghistorian --password $tag_historian_pwd --gzip C:\migration\mongo-dump\nitaghistorian
.\mongorestore.exe --port 27018 --db niopcclient --username niopcclient --password $opc_pwd --gzip C:\migration\mongo-dump\niopcclient
cd "C:\Program Files\National Instruments\Shared\Skyline"
.\NISystemLinkServerConfigCmd.exe stop-all-services
Copy-Item "C:\migration\keyvaluedb\dump.rdb" -Destination "C:\ProgramData\National Instruments\Skyline\KeyValueDatabase"
Copy-Item "C:\migration\OpcClient" -Destination "C:\ProgramData\National Instruments\Skyline\Data" -Recurse -force
cd "C:\Program Files\National Instruments\Shared\Skyline"
.\NISystemLinkServerConfigCmd.exe start-all-services