from django.shortcuts import render


def home_page(request):
    return  render(request, 'home_page.html')

def custom_404(request):
    return render(request, '404.html')

def custom_500(request):
    return render(request, '500.html')