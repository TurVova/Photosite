from django.urls import path
from blog import views

urlpatterns = [
    path('account/registration', views.register, name='register')
]