from django.urls import path

from .views import home_view, contact_view, login_view, register_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
]