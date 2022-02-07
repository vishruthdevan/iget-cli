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


def debug_access_token():
    params = get_creds()
    endpoint_params = dict()
    endpoint_params['input_token'] = params['access_token']
    endpoint_params['access_token'] = params['access_token']

    url = params['graph_domain'] + '/debug_token'

    response = make_api_call(url, endpoint_params)
    print(response)


def get_user_pages():
    params = get_creds()
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']

    url = params['endpoint_base'] + 'me/accounts'

    response = make_api_call(url, endpoint_params)

    print("Page Name:")
    print(response['json_data']['data'][0]['name'])
    print("\nPage Category:")
    print(response['json_data']['data'][0]['category'])
    print("\nPage Id:")
    print(response['json_data']['data'][0]['id'])


def get_instagram_account():
    params = get_creds()
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']
    endpoint_params['fields'] = 'instagram_business_account'

    url = params['endpoint_base'] + params['page_id']

    response = make_api_call(url, endpoint_params)
    # return response
    print("Page Id:")
    print(response['json_data']['id'])
    print("\nInstagram Business Account Id:")
    print(response['json_data']['instagram_business_account']['id'])
