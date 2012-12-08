from trakc.api.base import TrakcBaseResource
from trakc.models import Target
from django.db.models import Q

from tastypie import http
from tastypie.exceptions import ImmediateHttpResponse as ihr

class TargetResource(TrakcBaseResource):

    class Meta(TrakcBaseResource.Meta):
        queryset = Target.objects.all()
        resource_name = 'target'

    def obj_get_list(self, request=None, **kwargs):
        user = request.user
        #return Target.objects.filter(~Q(id__in=<mycampaign>.targeted_by.all())
        return Target.objects.filter(id__in=[u.id for u in user.targeted_by.all()])

    def obj_create(self, bundle, request=None, **kwargs):
        photo_url = bundle.data.get('photo_url', '')
        google_id = bundle.data.get('google_id', None)
        name = bundle.data.get('name', None)

        if google_id and name is None:
            raise ihr(http.HttpForbidden('Id or name not provided'))

        try:
            # Search in database to not add duplicates
            target = Target.objects.get(google_id=google_id)
        except:
            target = Target(
                    google_id=google_id,
                    target_photo=photo_url,
                    name=name
                )
            target.save()

        request.user.targeted_by.add(target.id)

        return bundle

    def obj_delete(self, request=None, **kwargs):
        target_id = kwargs.get('pk', None)

        if target_id is None:
            raise ihr(http.HttpForbidden('You do not have access to delete this target'))

        try:
            target = Target.objects.get(google_id=target_id)
        except:
            raise ihr(http.HttpForbidden('You do not have access to delete this target'))

        request.user.targeted_by.remove(target)

