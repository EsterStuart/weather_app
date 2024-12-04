from django.db import models

import requests
import json


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class WeatherReport(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    
    feels_like = models.CharField(max_length=100)
    
    def get_weather(City = "Marietta"):
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        API_KEY = "aa0066bc1a9eb434b15cf3e46027778f"
        URL = BASE_URL + "q=" + City + "&appid=" + "API_KEY" + "&units=imperial"
        
        response = requests.get(URL)
        # checking the status code of the request
        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # getting feels like
            feels_like = main['feels_like']
            city = City
                
        
        
    
    