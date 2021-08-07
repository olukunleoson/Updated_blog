from django.contrib import admin
from django.urls import path, include
from bloghome import views
import bloghome

urlpatterns =  [
    path('home/', views.home, name='home'),
    path('forum/', views.forum, name='forum'),
    path('human_right/', views.human_right, name='human_right'),
    path('anti_corruption/', views.anti_corruption, name='anti_corruption'),
    path('contact/', views.contact, name='contact'),
    path('centers/', views.centers, name='centers'),
    path('agent/', views.agent, name='agent'),
    path('technology/', views.technology, name='technology'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]