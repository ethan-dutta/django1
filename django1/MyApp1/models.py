from django.db import models

# Create your models here.

class teacher (models.Model):
    tch_id=models.IntegerField(primary_key=true)
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
    def __str__(self):
        return self.Name

