from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from account.forms import RegistrationForm, LoginForm


class Login(LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm
    
class Logout(LogoutView):
    next_page = 'home'

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'account/registration.html', {'form': form})