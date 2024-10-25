# Crating nwe file for urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # views.home is mean which response is send we write response we write in views file
    path('contact/', views.contact, name='contact'),   
]