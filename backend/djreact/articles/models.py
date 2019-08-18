from django.db import models

# Create your models here.
class Stocks(models.Model):
    label = models.CharField(max_length=50)
    values = models.IntegerField(default=0)

    def __str__(self):
        return self.label
