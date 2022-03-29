from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class teacherlogin(models.Model):
    teacherid=models.CharField(max_length=20)
    teacherpwd=models.CharField(max_length=15, validators=[
            MinLengthValidator(8, 'the field must contain at least 50 characters')
            ])
