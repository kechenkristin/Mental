from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Record(models.Model):
    submitter = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='submitted_events',
    )

    record_date = models.DateField(null=True)
    record = models.TextField(null=True)