import pprint
from utils import *


def get_business_discovery(params):
    endpoint_params = dict()
    endpoint_params['access_token'] = params['access_token']
    url = params['endpoint_base'] + \
        params['instagram_account_id']

    endpoint_params['fields'] = f"business_discovery.username({params['id']}){'{followers_count,media_count, media{permalink, comments_count, like_count}}'}"

    return make_api_call(url, endpoint_params)
