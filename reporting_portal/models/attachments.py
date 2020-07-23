from django.db import models

from reporting_portal.models.observation import Observation


class Attachments(models.Model):
    name = models.CharField(max_length=100)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)