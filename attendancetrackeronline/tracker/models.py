from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    minutes = models.BigIntegerField()
    days = models.JSONField(default=list)
    days_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name