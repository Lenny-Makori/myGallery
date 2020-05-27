from django.test import TestCase
from .models import categories, location, Image

# Create your tests here.
class ImageTest(TestCase):
    def setUp(self):
        self.new_location = Location(location_name='Naivasha')
        self.new_location.save()
        self.new_category = Category(category_name='vacation')
        self.new_category.save()

       self.image = Image(image_name='Fashion', image_description='menswear', image_location=self.new_location, image_category=self.new_category)
       self.image.save_image()

    
