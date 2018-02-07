from django.shortcuts import render, redirect

from blog.forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
        context = {'form' : form}
        return render(request, 'blog/registration.html', context)
