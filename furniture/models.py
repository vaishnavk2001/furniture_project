from django.db import models


# Create your models here.
class furniture(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pictures')
    material = models.CharField(max_length=50,default=None)
    desc = models.TextField(default=None)

