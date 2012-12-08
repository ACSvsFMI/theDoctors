from django.db import models
from json_field import JSONField

class Post(models.Model):
    
    class Meta:
        app_label = 'trakc'

    author = models.ForeignKey('Target')

    post_date = models.DateTimeField('date posted')

    content = JSONField(default={})
    
    likes = models.IntegerField(default=0)

    shares = models.IntegerField(default=0)

    comments = models.IntegerField(default=0)
