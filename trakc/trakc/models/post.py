from django.db import models
from json_field import JSONField

class Post(models.Model):
    
    class Meta:
        app_label = 'trakc'

    author = models.ForeignKey('Target', null=True, blank=True)

    google_id = models.CharField(max_length=64, null=True, blank=True)

    post_date = models.DateTimeField('date posted', null=True, blank=True)

    content = JSONField(default={}, null=True, blank=True)
    
    likes = models.IntegerField(default=0, null=True, blank=True)

    shares = models.IntegerField(default=0, null=True, blank=True)

    comments = models.IntegerField(default=0, null=True, blank=True)
