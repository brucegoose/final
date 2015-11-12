from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Investment(models.Model):
  company = models.TextField(null=True, blank=True)
  market = models.CharField(max_length=4)
  option = models.TextField(null=True, blank=True)
  price = models.IntegerField(6)
  volume = models.IntegerField(6)
  explanation = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title