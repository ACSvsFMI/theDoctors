from django.db import models
from json_field import JSONField

class Post(models.Model):
    
    class Meta:
        app_label = 'trakc'

    author = models.ForeignKey(Target)

    post_date = models.DateTimeField('date posted')
    
    actions = models.ManyToMany()

    targeted_by = models.ManyToMany(Action, through=ActionsAndPosts)

class ActionsAndPosts(models.Model):
    
    action = models.ForeignKey(Action)
    post = models.ForeignKey(Post)

    action_count = models.IntegerField(default=0)
