from django.db import models

# Create your models here.
class Company(models.Model):
    name = model.Charfield(max_length=100)

    def __str__(self):
        return self.name

class Envelope(model.Model):
    amount = models.IntegerField()
    motivation = models-Charfield(max_length=100)
    company = models.ForeignKey(Company, on_delete=model.CASCADE)

    def __str__(self):
    return self.company.name+" * "+self.motive
