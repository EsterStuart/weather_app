from .models import WeatherReport
from django.views.generic import ListView
from .forms import MyForm
from .api import get_key

import requests

from django.template.response import TemplateResponse

def get_weather(city):
	BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
	URL = BASE_URL + "q=" + city + "&appid=" + get_key() + "&units=imperial"
	response = requests.get(URL)
	print(response.status_code)
	if response.status_code == 200:
		data = response.json()
		return (data)
	else:
		return False
	
 
def weather_lookup(request):
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid():
			data = get_weather(form.cleaned_data['city'])
   
			main_values = data['main']
			weather_values = data['weather']
			visibility_values = data['visibility']
			wind_values = data['wind']
			sys_values = data['sys']
			timezone_values = data['timezone']
			name_values = data['name']
   
   
			return TemplateResponse(request, 'index.html', {'main_values' : main_values, 'weather_values' : weather_values, 'visibility_values' : visibility_values, 'wind_values' : wind_values,'sys_values' : sys_values, 'timezone_values' : timezone_values, 'name_values' : name_values})
	return TemplateResponse(request, 'index.html', {})

 
