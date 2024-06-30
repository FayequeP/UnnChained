import os
from urllib import response
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def getCreds():
    creds = dict()
    creds['access_token'] = os.getenv('ACCESS_TOKEN')
    creds['client_id'] = os.getenv('APP_ID')
    creds['client_secret'] = os.getenv('APP_SECRET')
    creds['graph_domain'] = os.getenv('GRAPH_DOMAIN')
    creds['graph_version'] = os.getenv('GRAPH_VERSION')
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' #dont worry about the error, it still works
    creds['debug'] = 'no'
    creds['page_id'] = '311373352057743'
    creds['instagram_account_id'] = '17841457199245717'
    creds['ig_username'] = 'taishin_dojo'
    creds['ig_media_id'] = '17933409164606944'
    return creds

def makeApiCall(url, endpointParams, debug = 'no'):
    data = requests.get(url, endpointParams)
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent=4)
    response['json_data'] = json.loads( data.content)
    response['json_data_pretty'] = json.dumps( response['json_data'], indent=4)
    
    if ('yes' == debug):
        displayApiCallData(response)
        
    return response

def displayApiCallData(response):
    print("\n URL:")
    print(response['url'])
    print("\n EndPoint Params:")
    print(response['endpoint_params_pretty'])
    print("\n Response:")
    print(response['json_data_pretty'])
     