from django.shortcuts import redirect, render
from .models import Produit,Commande
from  django.core.paginator import Paginator
from  django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'shop/accueil.html')
@login_required
def  menu(request):
    produit_object=Produit.objects.all() #je selectionne tous les produits de la base de donnee #
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
         produit_object= Produit.objects.filter(title__icontains=item_name)
    paginator=Paginator( produit_object, 4)    
    page=request.GET.get('page')
    produit_object=paginator.get_page(page)
    return render (request,'shop/index.html',{'produit_object':produit_object})
def detail (request,myid):
     produit_object=Produit.objects.get(id=myid)
     return render (request,'shop/detail.html',{'produit':produit_object})
# myshop/views.py
from django.shortcuts import render

def accueil_view(request):
    # Logique de votre vue d'accueil
    # ...

    # Renvoyer la réponse
    return render(request, 'index.html')
def paypay_view(request):
     return render(request, 'shop/paypal.html')

def checkout(request):
     if request.method=="POST":
          items=request.POST.get('items')
          total=request.POST.get('total')
          nom=request.POST.get('nom')
          email=request.POST.get('email')
          commune=request.POST.get('commune')
          zone=request.POST.get('zone')
         
          telephone=request.POST.get('telephone')
          commentaire=request.POST.get('commentaire')
          com= Commande(item=items,total=total, nom=nom, email=email, commune=commune, zone=zone, telephone=telephone, commentaire=commentaire)
          com.save()
          return redirect('paypal')  # Assurez-vous que 'paypal' est le bon nom d'URL
     return render(request, 'shop/checkout.html')
def confirmation(request):
    commandes = Commande.objects.all().order_by('-date_commande')[:1]
    context = {
        'commandes': commandes
    }
    return render(request, 'shop/confirmation.html', context)
def afficher(request):
        commandes= Commande.objects.all()
        return render(request, 'shop/confirmation.html', {'commandes': commandes})
from django.http import HttpResponse

from django.template.loader import render_to_string

