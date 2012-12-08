from django.db import models
from django.contrib.auth.models import User
from json_field import JSONField

class Action(models.Model):
    
    class Meta:
        app_label = 'trakc'

    name = models.CharField(max_length=16)
    
    cost = models.ManyToMany(User, through=UsersAndActions)

class ActionsAndPosts(models.Model):
    
    user = models.ForeignKey(User)
    action = models.ForeignKey(Action)

    action_cost = models.IntegerField(default=1)