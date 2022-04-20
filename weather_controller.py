import requests


def weather(city):    
    url = "https://wttr.in/" + city + "?format=3"

    weather_parameters = {
        "0":"",
        "m":"",
        "M":"",                
        "lang":"ru"        
    }

    response = requests.get(url, params=weather_parameters)  
    return response.text