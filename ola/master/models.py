from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

class CustDtil(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=250)
    user_lastname = models.CharField(max_length=250)
    user_add = models.CharField(max_length=250)
    user_long = models.IntegerField(default=0)
    user_lat = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Cust_ID)


class DriverDtil(models.Model):
    Driver_ID = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=250)
    user_lastname = models.CharField(max_length=250)
    user_add = models.CharField(max_length=250)
    user_long = models.CharField(max_length=250)
    user_lat = models.CharField(max_length=250)

    def __str__(self):
        return str(self.Driver_ID)

class Request_id(models.Model):

    Cust_ID = models.ForeignKey(CustDtil, on_delete=models.CASCADE)
    Driver_ID = models.ForeignKey(DriverDtil, on_delete=models.CASCADE, null=True)
    req_time = models.DateTimeField(auto_now_add=True)
    pickup = models.DateTimeField(null=True, blank=True)
    drop = models.DateTimeField(null=True, blank=True)
    Status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.Driver_ID)
