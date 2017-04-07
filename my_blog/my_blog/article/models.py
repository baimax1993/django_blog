from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150)
    catagory = models.CharField(max_length = 50, blank = True)
    datatime = models.DateField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)
    preface = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title