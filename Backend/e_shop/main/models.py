
from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
    
    def __str__(self):
        return self.title

class Brand(models.Model): 
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")

    def __str__(self): 
        return self.title

class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Size(models.Model): 
    title=models.CharField(max_length=100)

    def __str__(self): 
        return self.title
