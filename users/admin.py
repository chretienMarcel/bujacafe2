from django.contrib import admin
from .models import ProfileModel
from .models import Client


# Register your models here.
admin.site.register(ProfileModel)
list_display="username","email address","image",

#class ClientAdmin(admin.ModelAdmin):
    #list_display = ('id', 'username', 'nom', 'prenom', 'email')  # Affiche l'ID et d'autres champs
