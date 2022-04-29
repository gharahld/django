from django.db import models

# Create your models here.
class Pages(models.Model):
    tittle = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    featured = models.BooleanField() #null=True,default=True
