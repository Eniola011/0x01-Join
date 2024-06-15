from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login_signup/', views.login_signup, name='login_signup'),
]
