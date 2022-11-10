from django.contrib  import admin
from django.urls import path, include
from Geri import views

urlpatterns = [
    path('', views.index , name='index'),
    path('test', views.test , name='test'),
    path('about', views.about , name='about'),
    path('MiniCog', views.MiniCog , name='MiniCog'),
    path('Mns', views.Mns , name='Mns'),
    path('Gds', views.Gds , name='Gds'),
    
]
