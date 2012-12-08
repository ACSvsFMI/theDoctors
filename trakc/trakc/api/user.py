from django.contrib.auth.models import User
from trakc.api.base import TrakcBaseResource

class UserResource(TrakcBaseResource):

	class Meta(TrakcBaseResource.Meta):
		queryset = User.objects.all()
		resource_name = 'user'

