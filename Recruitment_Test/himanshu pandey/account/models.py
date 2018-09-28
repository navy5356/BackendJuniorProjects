from django.db import models


# Create your models here.
class bankaccount(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=50)
    balance=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    img=models.CharField(max_length=100000000000000000,default="https://www.google.co.in/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi8u_Gj_fbcAhWKpo8KHTXeBvYQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3ARBS_logo.svg&psig=AOvVaw0RYDi2wAr9EkbDY3QhjNrg&ust=1534694661442463")

    def __str__(self):
        return self.name


