from django.urls import path
from menu import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
]