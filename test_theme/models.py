from django.db import models
from django.utils import timezone

    
class Users(models.Model):
    
  u_name = models.CharField(max_length=10)
  u_password = models.CharField(max_length=255)
  u_ticket = models.CharField(max_length=30, null=True)

  
'''
  class Meta:
      managed = False
      db_table = 'db1'
'''
