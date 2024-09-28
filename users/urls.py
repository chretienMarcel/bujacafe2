from django.urls import path
from .import views
from django.contrib.auth import views as auth_view
from .views import change_password
from .views import delete_account


urlpatterns =[
   path('sign_up/',views.sign_up,name='users-sign-up'), 
   path('profile/',views.profile,name='users-profile'),
   path('login/',auth_view.LoginView.as_view(template_name='shop/users/login.html'),
        name='users-login'),
   path('logout/', auth_view.LogoutView.as_view(), name='logout'),  
   path('change-password/', change_password, name='change_password'), 
   path('delete-account/', delete_account, name='delete_account'),

   



]