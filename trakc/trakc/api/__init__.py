from user import UserResource
from target import TargetResource
from post import PostResource

from tastypie.api import Api

trakc_api = Api(api_name='v1')
trakc_api.register(UserResource())
trakc_api.register(TargetResource())
trakc_api.register(PostResource())

