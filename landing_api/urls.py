from django.urls import path
from .views import LandingAPI

urlpatterns = [
    # La ruta será /landing/api/index/
    path('index/', LandingAPI.as_view(), name='index'),
]