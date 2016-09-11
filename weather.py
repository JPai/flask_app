# -*- coding: utf-8 -*-

import forecastio
from geopy.geocoders import Nominatim

import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


#api_key = os.environ.get('API_KEY')
#address = "Taipei City, TW"

def get_weather(address):
    api_key = os.environ.get('FORECASTIO_API_KEY')
    geolocator = Nominatim()
    location = geolocator.geocode(address, timeout=10)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)

#print(get_weather(address, api_key))
