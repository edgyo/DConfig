from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='configurator.home'),
    path('config/<int:id>', views.config, name='configurator.configs'),
    path('home', views.home, name='configurator.home'),
    path('configurator', views.configurator, name='configurator.configurator'),
    path('components', views.components, name='configurator.components'),
    path('configs', views.configs, name='configurator.configs'),
]