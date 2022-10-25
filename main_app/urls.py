from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('change-password/', views.password_change, name='password_update'),
    path('profile/', views.profile_detail, name = 'profile_detail'),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name = 'profile_update'),
    path('food/create/', views.FoodCreate.as_view(), name='food_create'),
    path('food/', views.food_index, name='food_index'),
    path('food/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
    path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
]