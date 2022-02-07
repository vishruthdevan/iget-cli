import json
import requests
import json


def get_creds():
    creds = dict()
    creds['access_token'] = json.load(
        open("credentials.json", "r"))['access_token']
    creds['client_id'] = '2233159383499423'
    creds['client_secret'] = 'e9a6122388aa26d71fe693c35d0b0f6f'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v12.0'
    creds['endpoint_base'] = creds['graph_domain'] + \
        creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_name'] = 'vishruth.devan234'
    creds['page_id'] = '105316455408894'
    creds['instagram_account_id'] = '17841451798640055'
    creds['instagram_username'] = 'vishruth.devan234'

    return creds


def make_api_call(url, endpoint_params, method="GET"):

    if method == "POST":
        data = requests.post(url, endpoint_params)
    else:
        data = requests.get(url, endpoint_params)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpoint_params
    response['json_data'] = json.loads(data.content)

    return response['json_data']

