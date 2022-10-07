from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    county = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=13, null=True)

    USERNAME_FIELD = 'username'

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    agent = models.ForeignKey(User, related_name='clients', on_delete= models.DO_NOTHING, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_imei = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=20)
    # start_date = models.DateField()
    # end_date = models.DateField()

    def __str__(self):
        return self.email