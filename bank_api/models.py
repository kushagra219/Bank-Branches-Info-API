from django.db import models

# Create your models here.

class banks(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class branches(models.Model):
    bank = models.ForeignKey(banks, on_delete=models.CASCADE, related_name='bank_name')
    ifsc = models.CharField(max_length=11)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    def __str__(self):
        return "{} {}".format(self.bank.name, self.ifsc)


    