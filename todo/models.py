from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, related_name='todo',on_delete=models.CASCADE)
    completed =  models.BooleanField("Completed", blank=True, default=False)
    def __unicode__(self):
        return "%s" %self.name
