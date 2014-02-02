from django.db import models


class NestTemperatureReading(models.Model):
    when = models.DateTimeField(unique=True)
    measurement = models.FloatField()

class NestHumidityReading(models.Model):
    when = models.DateTimeField(unique=True)
    measurement = models.FloatField()

class NestTemperatureTarget(models.Model):
    when = models.DateTimeField(unique=True)
    target = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()

class NestHumidityTarget(models.Model):
    when = models.DateTimeField(unique=True)
    target = models.FloatField()
    min = models.FloatField(null=True)
    max = models.FloatField(null=True)
