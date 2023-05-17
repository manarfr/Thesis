from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Patient, Doctor

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'usermanagement/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if hasattr(user, 'patient'):
            context['user_type'] = 'patient'
            context['user_info'] = user.Patient
        elif hasattr(user, 'doctor'):
            context['user_type'] = 'doctor'
            context['user_info'] = user.Doctor
        return context


class UserLoginView(LoginView):
    template_name = 'usermanagement/login.html'
    success_url = reverse_lazy('dashboard')  # Redirect to dashboard page after successful login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'usermanagement/signup.html', {'form': form})

def home(request):
    return render(request, 'usermanagement/home.html')