from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Insuranced(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_imei = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.email