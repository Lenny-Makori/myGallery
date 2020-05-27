from django.test import TestCase
from .models import categories, location, Image

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.new_location = Location(location_name='Naivasha')
        self.new_location.save()
        self.new_category = Category(category_name='vacation')
        self.new_category.save()

       self.image = Image(image="image.jpg", image_name='Model', image_description='modelling', image_location=self.new_location, image_category=self.new_category)
       self.image.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        location.objects.all().delete()
        categories.objects.all().delete()

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_update_method(self):
        self.image.save_image()
        new_image = Image.objects.filter(image='image.jpg').update(image='new_image.jpg')
        images = Image.objects.get(image='new_image.jpg')
        self.assertTrue(images.image, 'new_image.jpg')

    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    

