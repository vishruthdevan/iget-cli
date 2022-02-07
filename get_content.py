import pprint
from utils import *


def get_business_discovery(params):
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']
    url = params['endpoint_base'] + \
        params['instagram_account_id']

    endpoint_params['fields'] = f"business_discovery.username({params['id']}){'{followers_count,media_count, media{permalink, comments_count, like_count}}'}"

    return make_api_call(url, endpoint_params)


def get_user_media(params):
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']
    url = params['endpoint_base'] + \
        params['instagram_account_id']

    endpoint_params['fields'] = f"business_discovery.username({params['id']}){'{media{permalink,media_url,caption,media_type,comments_count, like_count}}'}"

    return make_api_call(url, endpoint_params)


def get_media_details(params):
    for post in get_user_media(params)['business_discovery']['media']['data']:
        if post['permalink'] == params["permalink"]:
            return post


def get_user_data(params):
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']
    url = params['endpoint_base'] + \
        params['instagram_account_id']

    endpoint_params['fields'] = f"business_discovery.username({params['id']}){'{biography ,id,ig_id, followers_count, follows_count, media_count, name, profile_picture_url, username, website}'}"
    return make_api_call(url, endpoint_params)


# params = get_creds()
# params['id'] = 'bluebottle'
# params['media_id'] = "17895229742362082"
# pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(get_user_media(params))
