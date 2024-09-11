from django.urls import path
from steakhouse.views import index, detail,checkout,confirmation
from .import views

urlpatterns=[
    path('',index,name='home'),
    path('<int:myid>',detail,name='detail'),
    path('', views.accueil_view, name='nom_url_accueil'),
    
    path('menu/', views.menu, name='menu'),
    path('checkout', checkout,name='checkout'),
    path('confirmation', confirmation,name="confirmation"),
    
   
]
