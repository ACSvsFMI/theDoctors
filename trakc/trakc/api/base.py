from tastypie import http
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer

from trakc.api.lib import TrakcAuthentication

class TrakcResourceResponses(object):
    '''
        This class implements methods that should be called when something is
        not supposed to happen (an unauthorized user tries to access a resourse,
        an user tries to access a resource from LIMBO etc)
    '''

    def raise_unauthorized(self):
        '''
            Raise HttpUnauthorized
        '''
        raise ImmediateHttpResponse(http.HttpUnauthorized())

    def raise_forbidden(self):
        '''
            Raise HttpForbidden
        '''
        raise ImmediateHttpResponse(http.HttpForbidden())

class TrakcBaseResource(ModelResource, TrakcResourceResponses):
    '''
        WantydResource should provide methods and fields available for every
        other resource defined
    '''
    class Meta:
        authentication = TrakcAuthentication()
        authorization = Authorization()
        default_format = 'application/json'
        serializer = Serializer(formats=['json'])
        always_return_data = True
        export_allowed_methods = []

