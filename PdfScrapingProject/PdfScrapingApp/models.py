from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InsertDataModel(models.Model):
    user_select = models.ForeignKey(User,on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    observation_values = models.FloatField(blank=True,null=True)
    months = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return f'{self.user_select} {self.test_name}'
