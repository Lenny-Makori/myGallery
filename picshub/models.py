from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    