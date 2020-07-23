from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

    
class Users(models.Model):
    
  u_name = models.CharField(max_length=10)
  u_password = models.CharField(max_length=255)
  u_ticket = models.CharField(max_length=30, null=True)  
'''
  class Meta:
      managed = False
      db_table = 'db1'
'''

class ex_excel(models.Model):
  Name = models.CharField(max_length=50)
  Position = models.CharField(max_length=50)
  Office = models.CharField(max_length=50)
  Age = models.IntegerField(default=1,
                            validators=[MaxValueValidator(100),
                                        MinValueValidator(1)])
  Start_date = models.DateField()
  Salary = models.IntegerField(default=1)

  def __str__(self):
    return self.Name
'''
  class Meta:
    db_table = 'Ex_excel'
    managed = False
'''
