from django.urls import  path

from src.users.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view())
]