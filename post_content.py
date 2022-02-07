import pprint
from utils import *


def create_media_object(params):
    url = params['endpoint_base'] + \
        params['instagram_account_id'] + '/media'

    endpoint_params = dict()
    endpoint_params['caption'] = params['caption']
    endpoint_params['access_token'] = params['access_token']

    if 'IMAGE' == params['media_type']:
        endpoint_params['image_url'] = params['media_url']
    else:
        endpoint_params['media_type'] = params['media_type']
        endpoint_params['video_url'] = params['media_url']

    return make_api_call(url, endpoint_params, 'POST')


def get_media_object_status(media_id, params):
    url = params['endpoint_base'] + '/' + media_id

    endpoint_params = dict()
    endpoint_params['fields'] = 'status_code'
    endpoint_params['access_token'] = params['access_token']

    return make_api_call(url, endpoint_params, 'GET')
