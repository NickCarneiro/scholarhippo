from django.contrib import admin
from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Report(TimeStampedModel):
    problem = models.CharField(max_length=20)
    explanation = models.TextField()
    ip_address = models.IPAddressField()

    def __unicode__(self):
        return '{} -- {}'.format(self.created, self.problem)
