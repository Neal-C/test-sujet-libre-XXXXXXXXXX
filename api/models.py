from django.db import models

# Create your models here.

class Factory(models.Model):
    factoryName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.factoryName

class Bot(models.Model):
    botName = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    botFactory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return self.botName + " " + self.function