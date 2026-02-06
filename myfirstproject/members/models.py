from django.db import models
from django.utils.text import slugify

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
   
    def __str__(self):
        return f"{self.name} {self.email}"
    
class Meta(models.Model):
    car = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.car} {self.country}"  # Fixed: was referencing self.name which doesn't exist


# Create your models here.
