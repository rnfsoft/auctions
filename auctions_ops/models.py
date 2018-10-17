from django.db import models

# Create your models here.
class ManagementLog(models.Model):
    task = models.CharField(max_length=120)
    count = models.IntegerField(blank=True, null=True)
    started = models.DateTimeField(blank=True, null=True)
    finished = models.DateTimeField(blank=True, null=True)
    state_choices = (
        (1, "Starting"),
        (2, "In Progress"),
        (3, "Finished"),
    )
    state = models.IntegerField(choices=state_choices, blank=True, null=True)