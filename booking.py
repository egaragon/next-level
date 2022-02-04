from os import access
from square.client import Client


client = Client(
    access_token = 'EAAAEJrA6SYif4T2I73RCYSWTpAkZoXqBWxi6IPJZ5m8S_F1cL-CpbUNu2AmpQqe', #please hide this before going live
    environment = 'sandbox',
)

#get instance of Square API I want to call
api_locations = client.locations

#Call list_locations to get all locations in account
result = api_locations.list_locations()

#Call success if call succeeds
if result.is_success():
    #body property is list of locations
    locations = result.body['locations']
    #Iterate over list
    for location in locations:
        #Each location is represented as a dictionary
        for key, value in location.items():
            print(f'key {key} : value {value}')
        print('\n')
#Call error method to see if the call failed
elif result.is_error():
    print('Error calling API')
    errors = result.errors
    #Error is returned as a list
    for error in errors:
        #each error is a dictionary
        for key, value in error.items():
            print(f'key {key} : value {value}')
        print('\n')