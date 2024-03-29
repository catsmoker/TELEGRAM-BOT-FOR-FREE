import requests, json
from decouple import config

WEATHER_API_KEY = config('WEATHER')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


class City:
    def __init__(self,name,lon,lat):
        self.name = name #name of the city
        self.lon = lon #longitude 
        self.lat = lat #latitude



agadir = City("agadir ,IQ","-9.598107","30.427755")

limit = 5
URL = BASE_URL + "lat=" + agadir.lat + "&lon=" + agadir.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY

# HTTP request
def getCurrentWeather():

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
        # weather report
        report = data['weather']
        # print(f"{CITY:-^30}")
        # print(f"temp : {temperature} °C")
        # print(f"humind : {humidity} %")
        # print(f"prusser : {pressure} hPa")
        # print(f"report : {report[0]['description']} ")
        
        return f""" \n
        {agadir.name:-^30} \n
        درجة الحرارة : {temperature} °C\n
        الرطوبة : {humidity} %\n
        الضغط : {pressure} hPa\n
        {report[0]['description']}
        
        """
    else:
        # showing the error message
        print("Error in the HTTP request")
