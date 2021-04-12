from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('login',index),
    path('dasboard',index),
    path('telemovel', index)
]
