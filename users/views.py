from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomPasswordChangeForm, signupform,userupdateform,ProfileUpdateForm
from  django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = signupform()

    # Ligne à déplacer ici
    context = {
        'form': form,
    }
    return render(request, 'shop/users/sign_up.html', context)
@login_required
def profile(request):
    if request.method =='POST':
       u_form=userupdateform(request.POST or None,instance=request.user)
       p_form=ProfileUpdateForm(request.POST or None,request.FILES or None,instance=request.user.profilemodel)

       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           return redirect('users-profile')
    else:
        u_form =userupdateform(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context ={
        'u_form':u_form,
        'p_form':p_form,
    }    

    return render (request,'shop/users/profile.html',context)
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Garder l'utilisateur connecté
            messages.success(request, 'Votre mot de passe a été changé avec succès.')
            return redirect('users-login')  # Redirigez vers la page de profil ou une autre page
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'shop/users/change_password.html', {'form': form})
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()  # Supprimer l'utilisateur
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        return redirect('home')  # Redirigez vers la page d'accueil ou une autre page
    return render(request, 'shop/users/delete_account.html')