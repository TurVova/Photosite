from django.urls import path

from account import views
from account.views import Login, Logout

urlpatterns = [
    path('registration/', views.register, name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]



