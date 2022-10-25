from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile, Food, HealthRecord
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, Food
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
  return render(request,'base.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)  


@login_required
def profile_detail(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'profile/detail.html', {
    'profile': profile, 
    'user': request.user
  })


class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = ['name', 'calories', 'protein', 'carbohydrates', 'fats', 'sodium']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


@login_required
def food_index(request):
  foods = Food.objects.filter(user=request.user)
  return render(request, 'foods/index.html', { 'foods': foods })  

class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['age', 'height']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

@login_required
def password_change(request):
  error_message = ''
  if request.method == 'POST':
      form = PasswordChangeForm(user=request.user, data=request.POST)
      if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('/profile/')
      else:
        error_message = 'Invalid sign up - try again'
  form = PasswordChangeForm(user=request.user)
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/password-change.html', context)  

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'calories','protein', 'fats', 'carbohydrates', 'sodium']   

class HealthReordCreate(LoginRequiredMixin, CreateView):
  model = HealthRecord
  fields = ['weight', 'bodyfat']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class HealthRecordUpdate(LoginRequiredMixin, UpdateView):
  model = HealthRecord
  fields = ['weight', 'bodyfat']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form) 
  fields = ['name', 'calories','protein', 'fats', 'carbohydrates', 'sodium']    

class FoodDelete(DeleteView):
  model = Food
  success_url = '/food/' 
