import profile
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_detail, name = 'profile_detail'),
    path('food/create/', views.FoodCreate.as_view(), name='food_create'),
]