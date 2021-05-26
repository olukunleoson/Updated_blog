from django.contrib import admin
from django.urls import path, include
from bloghome import views
import bloghome

urlpatterns =  [
    path('/', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]