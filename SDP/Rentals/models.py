# from socket import SOL_NETROM
from xmlrpc.client import DateTime
from django.db import models
import datetime

class OnTheGo(models.Model):
    source = models.CharField(max_length = 200)
    destination = models.CharField(max_length = 200)
    cartype = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 60)
    def __str__(self):
        return 'From: '+self.source+' To: '+self.destination


class ScheduleRide(models.Model):
    source = models.CharField(max_length = 200)
    destination = models.CharField(max_length = 200)
    date = models.CharField(max_length = 30)
    time = models.CharField(max_length = 30)
    cartype = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 13)
    def __str__(self):
        return 'Date of travel: '+self.date



