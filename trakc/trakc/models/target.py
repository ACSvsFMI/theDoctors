from django.db import models
from django.contrib.auth.models import User

from json_field import JSONField

class Target(models.Model):
	
	class Meta:
		app_label = 'trakc'

	google_id = models.CharField(max_length=64,
					help_text='''The id to identify target on Google+''')
	
	name = models.CharField(max_length=64,
					help_text='''Name of target retrieved from social platform.
								Used to display it in interface''')

	target_photo = models.CharField(max_length=256, null=True, blank=True)

	targeted_by = models.ManyToManyField(User, through='UsersAndTargets', related_name='targeted_by')

class UsersAndTargets(models.Model):

	class Meta:
		app_label = 'trakc'

	user = models.ForeignKey(User)
	target = models.ForeignKey(Target)

	platform = JSONField(default={},
					help_text='''The platforms on which this a user spies a target''')

