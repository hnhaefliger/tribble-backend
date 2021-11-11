from django.db import models


class Session(models.Model):
    location = models.CharField(max_length=128)
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location
