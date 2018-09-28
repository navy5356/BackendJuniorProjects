from django.db import models
from django.core.validators import MinValueValidator

class Account ( models.Model):
    Name = models.CharField(max_length=200)
    Amount = models.DecimalField(decimal_places=2, max_digits=15, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return self.Name + " - " + str(self.Amount)


