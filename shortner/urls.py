from django.contrib import admin
from django.urls import path
from .views import Url, results, redirect
urlpatterns = [
    path('', Url.as_view(), name='home_view'),
    path('thanks/', results, name='results_view'),
    path('<slug:slug>/', redirect, name='redirect_view'),
]