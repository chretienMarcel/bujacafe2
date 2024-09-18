from django.db import models
from django.core.validators import FileExtensionValidator 

class Category(models.Model):
    nom=models.CharField(max_length=200)
    date_ajout=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_ajout']
    def __str__ (self):
        return self.nom



class Produit(models.Model):
    title=models.CharField(max_length=30)
    prix=models.FloatField()
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(default='default.png',upload_to='images',validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    date_ajout=models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_ajout']
    def __str__ (self):
        return self.title
class Commande(models.Model):
        item=models.CharField(max_length=200)
        total=models.CharField(max_length=200)
        nom=models.CharField(max_length=120)
        email=models.EmailField()
        adresse=models.CharField(max_length=200)
        ville=models.CharField(max_length=200)
        
        telephone=models.CharField(max_length=300)
        commentaire=models.TextField(default=0)
        date_commande=models.DateTimeField(auto_now=True)

        class Meta:
            ordering =['-date_commande']