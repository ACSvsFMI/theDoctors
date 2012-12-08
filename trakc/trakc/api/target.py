from trakc.api.base import TrakcBaseResource
from trakc.models import Target
from django.db.models import Q

class TargetResource(TrakcBaseResource):

	class Meta(TrakcBaseResource.Meta):
		queryset = Target.objects.all()
		resource_name = 'target'

	def obj_get_list(self, request=None, **kwargs):
		user = request.user
		#return Target.objects.filter(~Q(id__in=<mycampaign>.targeted_by.all())
		return Target.objects.filter(id__in=[u.id for u in user.usersandtargets_set.all()])

	