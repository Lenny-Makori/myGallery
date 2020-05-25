from django.db import models

# Create your models here.
class location(models.Model):
    pic_location = models.CharField(max_length=60)

    def __str__(self):
        return self.pic_location

class categories(models.Model):
    pic_category = models.CharField(max_length=60)

    def __str__(self):
        return self.pic_category

class Image(models.Model):
    image = models.ImageField(upload_to='image/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    image_location = models.ForeignKey(location)
    image_category = models.ManyToManyField(categories)

    def __str__(self):
        return self.image_name

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(title__icontains=search_term)
        return image