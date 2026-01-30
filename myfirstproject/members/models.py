from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

   
    def __str__(self):
        return f"{self.name} {self.email}"
    
class Meta(models.Model):
    car = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.car} {self.country}"  # Fixed: was referencing self.name which doesn't exist


# Create your models here.
