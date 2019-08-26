from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        self.sport = Category(name = 'Sport')

    def test_instance(self):
        self.assertTrue(isinstance(self.sport, Category))

    def tearDown(self):
        Category.objects.all().delete()

    def test_save_category(self):
        self.sport.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
       
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class LocationTestCase(TestCase):
    def setUp(self):
        self.spain = Location(name = 'Spain')

    def test_instance(self):
        self.assertTrue(isinstance(self.spain, Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_location(self):
        self.spain.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestCase(TestCase):
    def setUp(self):
        # Creating a new category and saving it
        self.new_category = Category(name = 'Sport')
        self.new_category.save_category()

        # Creat a new location and saving it
        self.new_location = Location(name = 'Spain')
        self.new_location.save_location()

        self.new_image = Image(name = 'Test Image',description = 'Test Description',category = self.new_category,location = self.new_location)
        self.new_image.save_image()

    def tearDown(self):
        Image.objects.all().delete()
    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


