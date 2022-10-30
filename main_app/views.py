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
from datetime import date

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
  data = HealthRecord.objects.filter(user=request.user).order_by('date')
  foods = Food.objects.filter(user=request.user, date=date.today())
  total_cals = 0
  total_protein = 0
  total_fat = 0
  total_carbs = 0
  total_sodium = 0
  for food in foods:
    total_cals += food.calories
    total_protein += food.protein
    total_fat += food.fats
    total_carbs += food.carbohydrates
    total_sodium += food.sodium

  return render(request, 'profile/detail.html', {
    'profile': profile, 
    'user': request.user,
    "data": data,
    'total_cals': total_cals,
    'total_protein': total_protein,
    'total_fat' : total_fat,
    'total_carbs' : total_carbs,
    'total_sodium' : total_sodium
  })

class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = ['name', 'calories', 'protein', 'carbohydrates', 'fats', 'sodium']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

@login_required
def food_index(request):
  foods = Food.objects.filter(user=request.user, date=date.today())
  return render(request, 'foods/index.html', { 'foods': foods })  

class ProfileUpdate(LoginRequiredMixin, UpdateView):
  model = Profile
  fields = ['age', 'height', 'daily_calories_goal']

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

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ['name', 'calories','protein', 'fats', 'carbohydrates', 'sodium']   

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/food/' 

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

@login_required
def food_history(request):
  if request.body:
      search = request.body.decode().split('&')[-1].split('=')[-1].split('-')
      search_date = date(int(search[0]), int(search[1]), int(search[2]))
      foods = Food.objects.filter(user=request.user, date=search_date)
      calories_consumed = 0
      for food in foods:
        calories_consumed+=food.calories
      return render(request, 'foods/history.html', {'date': search_date, 'foods': foods, 'calories_consumed': calories_consumed})
  else:
    return render(request, 'foods/history.html', {'foods': {}})  