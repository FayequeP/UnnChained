from defines import getCreds, makeApiCall

def getUserMedia(params, pagingUrl = ''):
    
    endpointParams = dict()
    endpointParams['access_token'] = params['access_token']
    endpointParams['fields'] = 'id,caption,media_url,permalink,thumbnail_url,timestamp,username'
    
    if ( '' == pagingUrl):
        url = params['endpoint_base'] + params['instagram_account_id'] + '/media'
    else:
        url = pagingUrl
        
    return makeApiCall(url, endpointParams, params['debug'])

params = getCreds()
params['debug'] = 'no'
response = getUserMedia(params)

params['debug'] = 'yes'
response = getUserMedia(params, response['json_data']['paging']['next'])


