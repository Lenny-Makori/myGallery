from django.db import models

# Create your models here.
class location(models.Model):
    pic_location = models.CharField(max_length=60)

class category(models.Model):
    pic_category = models.CharField(max_length=60)

class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    image_location = models.ForeignKey(location)
    image_category = models.ForeignKey(category)