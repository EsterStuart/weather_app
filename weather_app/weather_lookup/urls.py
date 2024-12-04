
from django.urls import path
from .views import weather_lookup
 
urlpatterns = [
    path('', weather_lookup, name='weather_lookup'),
]
