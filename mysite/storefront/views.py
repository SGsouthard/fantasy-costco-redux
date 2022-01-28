from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Weapon # WeaponForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group




# Create your views here.
def index(request):
    return render(request, 'base.html')



########### USER #############
def login_view(request):
    if request.method == 'POST':
        # try to log the user in
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user) # log the user in by creating a session
                    return redirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return redirect('/login')
        else:
            print('The username and/or password is incorrect.')
            return redirect('/login')
    else: # it was a GET request so send the empty login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Submission-Page-Permissions')
            user.groups.add(group)
            login(request, user)
            return redirect('/user/'+str(user))
        else:
            return HttpResponse('<h1>Signup Failed, Please Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    # Weapons = Weapon.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username,})


# def submit_weapon(request):
#     WeaponForm = modelformset_factory(Weapon, fields=('__all__'))
#     if request.method == 'POST':
#         form = WeaponForm(request.POST, request.FILES)
#         print(form, "testing the form inside the first if statement")
#         if form.is_valid():
#             form.save()
#             print(form, "testing if the second if statement is activating")
#         else:
#             print("first else has activated")
#             return HttpResponse('<h1>Submission Failed, please log in and try again!</h1>')

#     else:
#         form = WeaponForm()
#     return render(request, 'submit.html', {'form':form})

def WeaponViewAll(request):
    return HttpResponse('Testing for now')

class WeaponCreateView(CreateView):
    model = Weapon
    fields = ['name', 'description', 'price']

class WeaponUpdateView(UpdateView):
    model = Weapon
    fields = ['name', 'description', 'price']

class WeaponDeleteView(DeleteView):
    model = Weapon
    # success_url = reverse_lazy('')

