from django.contrib import admin
from .models import Category,Produit,Commande

admin.site.site_header="BUJACAFE"
#admin.site.site_title="MARCELSHOP"
admin.site.index_title="manageur"
class AdminCategorie(admin.ModelAdmin):
    list_display="nom","date_ajout"

class AdminProduit(admin.ModelAdmin):
    list_display="title","prix","category","date_ajout"
    search_fields=('title',)
    list_editable=("prix",)
class AdminCommande(admin.ModelAdmin):
    list_display=("item","nom","email","adresse","ville","pays","telephone","commentaire","total","date_commande")
admin.site.register(Category,AdminCategorie)
admin.site.register(Produit,AdminProduit)
admin.site.register(Commande,AdminCommande)