from django.urls import path
from .views import TelemovelView, UserView

urlpatterns = [
    path('user', UserView.as_view()),
    path('telemovel', TelemovelView.as_view()),
]