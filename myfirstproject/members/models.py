from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(null=True)

   
    def __str__(self):
        return self.name
    
class Meta(models.Model):
    car = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name


# Create your models here.
