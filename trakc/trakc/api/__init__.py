from user import UserResource

from tastypie.api import Api

trakc_api = Api(api_name='v1')
trakc_api.register(UserResource())

