from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from accounts.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="Categories/%Y/%m/%d/%h/%M/",default='static/images/laptops.png')
    def __str__(self):
        return f"{self.name.replace('-',' ').title()}"
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    rating = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    category = models.ForeignKey(Category,related_name="category" ,on_delete=models.CASCADE)
    thumbnail = models.URLField()


    def __str__(self):
        return f"{self.title}"
    


