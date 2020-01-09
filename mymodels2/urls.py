# mymodels2/urls.py

from django.urls import path, include
from .views import insert, input, display

app_name = 'mymodels2'

urlpatterns = [
    path('', input, name='input'),
    path('insert/', insert, name='insert'),
    path('display/', display, name='display')
]