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

    return render(request, 'index.html')

def submit_directory(request):
    return render(request, 'submit-directory.html')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'username': username,})

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = '/'

# ===== WEAPONS ===== #

class WeaponCreateView(LoginRequiredMixin, CreateView):
    model = Weapon
    fields = ['name', 'description', 'price']
    success_url = '/weapon/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class WeaponUpdateView(LoginRequiredMixin, UpdateView):
    model = Weapon
    fields = ['name', 'description', 'price']
    success_url = '/weapon/'


class WeaponDeleteView(LoginRequiredMixin, DeleteView):
    model = Weapon
    success_url = '/weapon/'

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
    success_url = '/armor/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ArmorUpdateView(LoginRequiredMixin, UpdateView):
    model = Armor
    fields = ['name', 'description', 'price']
    success_url = '/armor/'

class ArmorDeleteView(LoginRequiredMixin, DeleteView):
    model = Armor
    success_url = '/armor/'

def armor_index(request):
    armors = Armor.objects.all()
    return render(request, 'armor/index.html', {'armors': armors})

def armor_show(request, armor_id):
    armor= Armor.objects.get(id=armor_id)
    return render(request, 'armor/show.html', {'armor':armor})

# ===== Adventure Gear ===== #

class AdventureGearCreateView(LoginRequiredMixin, CreateView):
    model = AdventureGear
    fields = ['name', 'description', 'price']
    success_url = '/adventuregear/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class AdventureGearUpdateView(LoginRequiredMixin, UpdateView):
    model = AdventureGear
    fields = ['name', 'description', 'price']
    success_url = '/adventuregear/'

class AdventureGearDeleteView(LoginRequiredMixin, DeleteView):
    model = AdventureGear
    success_url = '/adventuregear/'

def adventuregear_index(request):
    adventuregears = AdventureGear.objects.all()
    return render(request, 'adventure-gear/index.html', {'adventuregears': adventuregears})

def adventuregear_show(request, adventuregear_id):
    adventuregear= AdventureGear.objects.get(id=adventuregear_id)
    return render(request, 'adventure-gear/show.html', {'adventuregear':adventuregear})

# ===== Mount ===== #

class MountCreateView(LoginRequiredMixin, CreateView):
    model = Mount
    fields = ['name', 'description', 'price']
    success_url = '/mount/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class MountUpdateView(LoginRequiredMixin, UpdateView):
    model = Mount
    fields = ['name', 'description', 'price']
    success_url = '/mount/'

class MountDeleteView(LoginRequiredMixin, DeleteView):
    model = Mount
    success_url = '/mount/'

def mount_index(request):
    mounts = Mount.objects.all()
    return render(request, 'mount/index.html', {'mounts': mounts})

def mount_show(request, mount_id):
    mount= Mount.objects.get(id=mount_id)
    return render(request, 'mount/show.html', {'mount':mount})

# ===== Potion ===== #

class PotionCreateView(LoginRequiredMixin, CreateView):
    model = Potion
    fields = ['name', 'description', 'price']
    success_url = '/potion/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PotionUpdateView(LoginRequiredMixin, UpdateView):
    model = Potion
    fields = ['name', 'description', 'price']
    success_url = '/potion/'

class PotionDeleteView(LoginRequiredMixin, DeleteView):
    model = Potion
    success_url = '/potion/'

def potion_index(request):
    potions = Potion.objects.all()
    return render(request, 'potion/index.html', {'potions': potions})

def potion_show(request, potion_id):
    potion= Potion.objects.get(id=potion_id)
    return render(request, 'potion/show.html', {'potion':potion})

# ===== Trinket ===== #

class TrinketCreateView(LoginRequiredMixin, CreateView):
    model = Trinket
    fields = ['name', 'description', 'price']
    success_url = '/trinket/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TrinketUpdateView(LoginRequiredMixin, UpdateView):
    model = Trinket
    fields = ['name', 'description', 'price']
    success_url = '/trinket/'

class TrinketDeleteView(LoginRequiredMixin, DeleteView):
    model = Trinket
    success_url = '/trinket/'

def trinket_index(request):
    trinkets = Trinket.objects.all()
    return render(request, 'trinket/index.html', {'trinkets': trinkets})

def trinket_show(request, trinket_id):
    trinket= Trinket.objects.get(id=trinket_id)
    return render(request, 'trinket/show.html', {'trinket':trinket})