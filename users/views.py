from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform

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