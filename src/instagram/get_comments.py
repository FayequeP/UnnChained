from defines import getCreds, makeApiCall
from get_user_media import getUserMedia

def getComments(params):
    
    endpointParams = dict()
    endpointParams['ig_media_id'] = params['ig_media_id']
    endpointParams['access_token'] = params['access_token']
    
    url = params['endpoint_base'] + params['ig_media_id'] + '/comments'
        
    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'yes'
response = getComments(params)



