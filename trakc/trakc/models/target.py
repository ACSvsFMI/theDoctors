from django.db import models
from django.contrib.auth.models import User

from json_field import JSONField

class Target(models.Model):
	
	class Meta:
		app_label = 'trakc'

	google_id = models.CharField(max_length=64,
					help_text='''The id to identify target on Google+''')

	facebook_id = models.CharField(max_length=64,
					help_text='''The id to identify target on Facebook''')
	
	name = models.CharField(max_length=64,
					help_text='''Name of target retrieved from social platform.
								Used to display it in interface''')

	targeted_by = models.ManyToMany(User, through=UsersAndTargets)

class UsersAndTargets(models.Model):
	
	user = models.ForeignKey(User)
	target = mdoels.ForeignKey(Target)

	platform = models.JSONField(default={},
					help_text='''The platforms on which this a user spies a target''')
