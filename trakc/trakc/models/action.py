from django.db import models
from django.contrib.auth.models import User

class Action(models.Model):
    
    class Meta:
        app_label = 'trakc'

    name = models.CharField(max_length=16)
    
    cost = models.ManyToManyField(User, through='UsersAndActions')

class UsersAndActions(models.Model):
    
    class Meta:
        app_label = 'trakc'

    user = models.ForeignKey(User)
    action = models.ForeignKey(Action)

    action_cost = models.IntegerField(default=1)

