from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    useruid = models.IntegerField(blank=True, null=True,default=0)
    completed =  models.BooleanField("Completed", blank=True, default=False)
    def __str__(self):
        return "%s" %self.name
