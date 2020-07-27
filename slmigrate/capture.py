from slmigrate import constants

def capture_mongo_data(service):
    print (service + " capture_mongo_data_called")
    

def capture_file_data(service):
    print (service + " capture_file_data called")



def capture_migration(service):
    print(service + " capture migration called")
    capture_mongo_data(service)
    if (service == constants.opcservice):
        capture_file_data(service)



    
