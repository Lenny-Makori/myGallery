from django.test import TestCase
from .models import categories, location, Image

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.new_location = location(location_name='Naivasha')
        self.new_location.save()
        self.new_category = categories(category_name='vacation')
        self.new_category.save()

    def tearDown(self):
        Image.objects.all().delete()
        location.objects.all().delete()
        categories.objects.all().delete()

    def test_init(self):
        self.assertTrue(isinstance(self.image, Image))