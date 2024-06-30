from defines import getCreds, makeApiCall

def getInstagramAccount(params):
    
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'instagram_business_account'
    
    url = params['endpoint_base'] + params['page_id']
    
    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'no'
response = getInstagramAccount(params)

print("Page Id:")
print(response['json_data']['id'])
print("Business Account Id:")
print(response['json_data']['instagram_business_account']['id'])