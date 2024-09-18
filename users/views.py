from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform,userupdateform,ProfileUpdateForm
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
