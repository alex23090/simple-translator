from django.urls import path
from . import views


urlpatterns = [
    path('', views.translationForm, name='home'),
]