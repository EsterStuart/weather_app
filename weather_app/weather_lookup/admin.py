from django.contrib import admin
from .models import WeatherReport
from .models import Product
# Register your models here.
admin.site.register(WeatherReport)
admin.site.register(Product)