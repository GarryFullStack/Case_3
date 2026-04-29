# urls.py
from django.urls import path
from myapp.views import index, welcome

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', welcome, name='welcome'),
]