from django.urls import path

from . import views
from storefront.views import WeaponCreateView, WeaponUpdateView, WeaponDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup_view, name='signup'),
    path('user/<username>/', views.profile, name='profile'),
    # path('submit-weapon', views.submit_weapon, name='submit-weapon'),
    path('weapon/add/', views.WeaponCreateView.as_view(), name='weapon-add'),
    path('weapon/<int:pk>/update/', views.WeaponUpdateView.as_view(), name='weapon-update'),
    path('weapon/<int:pk>/delete/', views.WeaponDeleteView.as_view(), name='weapon-delete'),
    path('weapons/', views.weapon_index, name='weapons'),
    path('weapon/<int:weapon_id/', views.weapon_show, name='weapon'),
]