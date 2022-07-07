from django.db import models
class branch(models.Model):
    name=models.CharField(max_length=25)
    batch=models.IntegerField()
    class timetable(models.Model):
        