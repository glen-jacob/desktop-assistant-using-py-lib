import requests
from ss import *

api_address = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=" + key
json_data = requests.get(api_address).json()

def news():
    ar = []
    for i in range(3):
        ar.append(str(i+1) + ", " + json_data["articles"][i]["title"] + ".")
    return ar

arr = news()



