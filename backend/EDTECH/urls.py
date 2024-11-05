
from django.urls import path
from .views import views

urlpatterns = [
    path('home/' , views.HomeView.as_view(), name='home'),
    path('logout/' , views.LogoutView.as_view(), name='logout')
]
