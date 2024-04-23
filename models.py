from django.db import models

class TemperaturePrediction(models.Model):
    apparent_temperature = models.FloatField()
    predicted_temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

