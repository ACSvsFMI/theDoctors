from trakc.api.base import TrakcBaseResource
from trakc.models import Post
from trakc.api import TargetResource
from tastypie import fields
from datetime import datetime

class PostResource(TrakcBaseResource):

	author = fields.ForeignKey(TargetResource, 'author', full=True)

	class Meta(TrakcBaseResource.Meta):
		queryset = Post.objects.all()
		resource_name = 'post'

	def obj_get_list(self, request=None, **kwargs):
		user = request.user
		#return Target.objects.filter(~Q(id__in=<mycampaign>.targeted_by.all())
		since = request.GET.get('since', '')
		until = request.GET.get('until', '')
		if (len(since) <= 1):
			since = '2008-01-01 00:00:01'
		else:
			since = datetime.fromtimestamp(int(since))
		if (len(str(until)) <= 1):
			until = datetime.now()
		else:
			since = datetime.fromtimestamp(int(until))
		return Post.objects.filter(author_id__in=[u.id for u in user.usersandtargets_set.all()], post_date__lte=until, post_date__gte=since)

	def dehydrate(self, bundle):
		#import pdb; pdb.set_trace()
		user = bundle.request.user
		post = bundle.obj
		action = user.action_set.all()[0]
		ref_ind = post.likes * action.like_cost + post.shares * action.share_cost + post.comments * action.comment_cost
		bundle.data['rel_data'] = str(ref_ind)
		return bundle
