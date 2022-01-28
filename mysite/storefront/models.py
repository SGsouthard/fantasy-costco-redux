from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.forms import ModelForm

DICE_CHOICES = [
    ('D4', 'd4'),
    ('D6', 'd6'),
    ('D8', 'd8'),
    ('D10', 'd10'),
    ('D12', 'd12'),
    ('D20', 'd20'),
    ('D100', 'd100'),
]

DAMAGE_CHOICES = [
    ('none', 'None'),
    ('basic', (
        ('bludg', 'Bludgeoning'),
        ('pierce', 'Piercing'),
        ('slash', 'Slashing'),
        )
    ),
    ('elemental', (
            ('cold', 'Cold'),
            ('fire', 'Fire'),
            ('force', 'Force'),
            ('light', 'Lightning'),
            ('thund', 'Thunder'),
        )
    ),
    ('acid', 'Acid'),   
    ('necro', 'Necrotic'),   
    ('poison', 'Poison'),
    ('psych', 'Psychic'),
    ('radiant', 'Radiant'),
]

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)
    price = models.CharField(max_length=50)

    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

# class WeaponForm(ModelForm):
#     class Meta:
#         model = Weapon
#         fields = ['name', 'description', 'price', 'amountofdice', 'dicetype', 'modifier', 'user']




class Armor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdventureGear(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mount(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Potion(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Trinket(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    # added automatically when a user creates something
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name