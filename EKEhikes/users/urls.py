from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name = 'logout'),
  #  path('register/', views.RegisterView.as_view(), name='register'),
]