from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/', null = True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null='True', blank=True)
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null='True', blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()   

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()
     
    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__name__icontains=search_input)
        return images 

class Category(models.Model):
    name = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(self):
        Category.objects.filter(id = self.pkcategory).delete()
    
    def update_category(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)    

class Location(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()
        
    @classmethod    
    def delete_location(self):
        Location.objects.filter(id = self.pk).delete()
   
    def update_location(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)     

    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images 

    @classmethod
    def image_locations(cls):
        images = cls.objects.order_by('location')
        return images 

    @classmethod
    def image_categories(cls):
        images = cls.objects.order_by('category')
        return images 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image


    class Meta:
        ordering = ['name']