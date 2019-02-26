from django.db import models

# Create your models here.
class Company(models.Model):
    name = model.Charfield(max_length=100)

class Envelope(model.Model):
    amount = models.IntegerField()
    motivation = models-Charfield(max_length=100)
    company = models.ForeignKey(Company)
