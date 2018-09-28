from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=200)
    account_balance = models.IntegerField(max_length=None)



