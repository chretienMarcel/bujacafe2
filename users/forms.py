from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
#from .models import ProfileModel


class signupform(UserCreationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
       
    )
    email= forms.EmailField(
        label=_("email"),
        max_length=150,
         help_text=_("type your email adress here:"),
       
    )
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Your password must contain at least 8 characters."),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
#class userupdateform(forms.ModelForm):
        class Meta:
            model= User
            fields=['username','email']
#class ProfileUpdateForm(forms.ModelForm):
        #class Meta:
            #model = ProfileModel
           #fields= ['image'] 

   