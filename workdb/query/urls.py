from django.urls import path
from .views import *

app_name = 'query'
urlpatterns = [
    path('queries/', main, name='home'),
]