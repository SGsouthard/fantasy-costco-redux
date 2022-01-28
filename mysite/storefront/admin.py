from django.contrib import admin
from .models import Weapon, Armor, AdventureGear, Mount, Potion, Trinket

# Register your models here.
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(AdventureGear)
admin.site.register(Mount)
admin.site.register(Potion)
admin.site.register(Trinket)