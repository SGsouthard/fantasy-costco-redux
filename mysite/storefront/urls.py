from django.urls import path

from . import views
from storefront.views import WeaponCreateView, WeaponUpdateView, WeaponDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    # Weapon Paths
    path('weapon/add/', views.WeaponCreateView.as_view(), name='weapon-add'),
    path('weapon/<int:pk>/update/', views.WeaponUpdateView.as_view(), name='weapon-update'),
    path('weapon/<int:pk>/delete/', views.WeaponDeleteView.as_view(), name='weapon-delete'),
    path('weapon/', views.weapon_index, name='weapons'),
    path('weapon/<int:weapon_id>/', views.weapon_show, name='weapon'),
    # Armor Paths
    path('armor/add/', views.ArmorCreateView.as_view(), name='armor-add'),
    path('armor/<int:pk>/update', views.ArmorUpdateView.as_view(), name='armor-update'),
    path('armor/<int:pk>/delete', views.ArmorDeleteView.as_view(), name='armor-delete'),
    path('armor/', views.armor_index, name='armors'),
    path('armor/<int:pk>/', views.armor_show, name='armor'),
    # Adventure Gear Paths
    path('adventuregear/add/', views.AdventureGearCreateView.as_view(), name='adventuregear-add'),
    path('adventuregear/<int:pk>/update', views.AdventureGearUpdateView.as_view(), name='adventuregear-update'),
    path('adventuregear/<int:pk>/delete', views.AdventureGearDeleteView.as_view(), name='adventuregear-delete'),
    path('adventuregear/', views.adventuregear_index, name='adventuregears'),
    path('adventuregear/<int:pk>/', views.adventuregear_show, name='adventuregear'),
    # Mount Paths
    path('mount/add/', views.MountCreateView.as_view(), name='mount-add'),
    path('mount/<int:pk>/update', views.MountUpdateView.as_view(), name='mount-update'),
    path('mount/<int:pk>/delete', views.MountDeleteView.as_view(), name='mount-delete'),
    path('mount/', views.mount_index, name='mounts'),
    path('mount/<int:pk>/', views.mount_show, name='mount'),
    # Potion Paths
    path('potion/add/', views.PotionCreateView.as_view(), name='potion-add'),
    path('potion/<int:pk>/update', views.PotionUpdateView.as_view(), name='potion-update'),
    path('potion/<int:pk>/delete', views.PotionDeleteView.as_view(), name='potion-delete'),
    path('potion/', views.potion_index, name='potions'),
    path('potion/<int:pk>/', views.potion_show, name='potion'),
    # Trinket Paths
    path('trinket/add/', views.TrinketCreateView.as_view(), name='trinket-add'),
    path('trinket/<int:pk>/update', views.TrinketUpdateView.as_view(), name='trinket-update'),
    path('trinket/<int:pk>/delete', views.TrinketDeleteView.as_view(), name='trinket-delete'),
    path('trinket/', views.trinket_index, name='trinkets'),
    path('trinket/<int:pk>/', views.trinket_show, name='trinket'),
]   