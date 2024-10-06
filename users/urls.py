from django.urls import path
#import views
from django.contrib.auth import views as auth_views #views de autenticação
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
