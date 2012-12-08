from django.db import models
from django.contrib.auth.models import User

class Action(models.Model):
    
    class Meta:
        app_label = 'trakc'

    user = models.ForeignKey(User)
    
    like_cost = models.IntegerField(default=1)
    share_cost = models.IntegerField(default=1)
    comment_cost = models.IntegerField(default=1)

