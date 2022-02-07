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


def publish_media(media_id, params):
    url = params['endpoint_base'] + params['instagram_account_id'] + \
        '/media_publish'

    endpoint_params = dict()
    endpoint_params['creation_id'] = media_id
    endpoint_params['access_token'] = params['access_token']

    return make_api_call(url, endpoint_params, 'POST')

# params = get_creds()
# params['media_type'] = "IMAGE"
# params['caption'] = "test"
# params['media_url'] = 'https://workmacro.com/wp-content/uploads/2018/02/4-by-5-819x1024.png'

# pp = pprint.PrettyPrinter(indent=2)

# # media_id = create_media_object(params)
# # print(media_id)
# publish_media('17919828491084241', params)
