from django.db import models

class AbortionData(models.Model):
    state=models.CharField(max_length=200)
    policy=models.TextField()
    