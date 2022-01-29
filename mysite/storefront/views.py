from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import Armor, Weapon, AdventureGear, Mount, Potion, Trinket
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin


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
    return render(request, 'profile.html', {'username': username,})

# ===== WEAPONS ===== #

class WeaponCreateView(LoginRequiredMixin, CreateView):
    model = Weapon
    fields = ['name', 'description', 'price']
    success_url = '/weapons/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class WeaponUpdateView(LoginRequiredMixin, UpdateView):
    model = Weapon
    fields = ['name', 'description', 'price']
    success_url = '/weapons/'


class WeaponDeleteView(LoginRequiredMixin, DeleteView):
    model = Weapon
    success_url = '/weapons/'

def weapon_index(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/index.html', {'weapons': weapons})

def weapon_show(request, weapon_id):
    weapon= Weapon.objects.get(id=weapon_id)
    return render(request, 'weapons/show.html', {'weapon':weapon})

# ===== ARMOR ===== #

class ArmorCreateView(LoginRequiredMixin, CreateView):
    model = Armor
    fields = ['name', 'description', 'price']
    success_url = '/armors/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ArmorUpdateView(LoginRequiredMixin, UpdateView):
    model = Armor
    fields = ['name', 'description', 'price']
    success_url = '/armors/'

class ArmorDeleteView(LoginRequiredMixin, DeleteView):
    model = Armor
    success_url = '/armors/'

def armor_index(request):
    armors = Armor.objects.all()
    return render(request, 'armor/index.html', {'armors': armors})

def armor_show(request, armor_id):
    armor= Armor.objects.get(id=armor_id)
    return render(request, 'armor/show.html', {'armor':armor})

# ===== Adventure Gear ===== #