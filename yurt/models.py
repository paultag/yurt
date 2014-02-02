from django.db import models


class NestTemperatureReading(models.Model):
    when = models.DateTimeField()
    measurement = models.FloatField()

class NestHumidityReading(models.Model):
    when = models.DateTimeField()
    measurement = models.FloatField()

class NestTemperatureTarget(models.Model):
    when = models.DateTimeField()
    target = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()

class NestHumidityTarget(models.Model):
    when = models.DateTimeField()
    target = models.FloatField()
    min = models.FloatField()
    max = models.FloatField()
