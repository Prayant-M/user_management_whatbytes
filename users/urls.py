from django.urls import path
from .views import home, RegisterView
from django.urls import path
from .views import profile

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]