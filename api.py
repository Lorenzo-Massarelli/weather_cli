import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    try:
        params = { "q": city,
                   "appid": API_KEY,
                   "units": "metric"
                   }
        
        r = requests.get(WEATHER_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    
    except requests.exceptions.RequestException as e:
        print("Error fetching weather: ", e)
        return None
    
    

def get_forecast(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
    
        r=requests.get(FORECAST_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()
    
    except requests.exceptions.RequestException as e:
        print("Error fetching forecast: ", e)
        return None