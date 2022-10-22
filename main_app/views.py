from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import Profile, Food
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm

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
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)