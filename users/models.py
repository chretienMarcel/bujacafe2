from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.webp',upload_to='profile',validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
def __str__(self):
    return self.user.username
# models.py

from django.db import models
from django.contrib.auth.hashers import make_password

class Client(models.Model):
    username = models.CharField(max_length=150, unique=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username