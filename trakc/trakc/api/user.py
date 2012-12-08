from django.contrib.auth.models import User
from trakc.api.base import TrakcBaseResource
from trakc.models import Action

class UserResource(TrakcBaseResource):
    '''
        The User Resource is only used to get/update the action weights
    '''

    class Meta(TrakcBaseResource.Meta):
        queryset = User.objects.all()
        resource_name = 'user'
        list_allowed_methods = []
        detail_allowed_methods = ['get', 'put']

    def obj_get(self, request=None, **kwargs):
        kwargs['pk'] = request.user.id
        return super(UserResource, self).obj_get(request, **kwargs)

    def dehydrate(self, bundle):
        try:
            action = bundle.request.user.action_set.all()[0]
        except:
            action = Action()
            action.like_cost = 1
            action.share_cost = 1
            action.comment_cost = 1
            action.user_id = bundle.request.user.id
            action.save()

        bundle.data.clear()
        bundle.data['like_cost'] = action.like_cost
        bundle.data['share_cost'] = action.share_cost
        bundle.data['comment_cost'] = action.comment_cost

        return bundle;

    def obj_update(self, bundle, request=None, **kwargs):
        try:
            action = bundle.request.user.action_set.all()[0]
        except:
            action = Action()
            action.user_id = bundle.request.user.id

        action.like_cost = bundle.data.get('like', 1) 
        action.share_cost = bundle.data.get('share', 1)
        action.comment_cost = bundle.data.get('comment', 1)
        action.save()

        return bundle
