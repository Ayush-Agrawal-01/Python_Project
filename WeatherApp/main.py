import requests #The requests module allows you to send HTTP requests using Python.
import json
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("Enter the name of the city : ")
url = f"https://api.weatherapi.com/v1/current.json?key=46dd97b295a74e5eaa9114903232804&q={city}"
r = requests.get(url)
wdict = json.loads(r.text)
print(wdict["current"]["temp_c"])
w = wdict["current"]["temp_c"]
speaker.Speak(f"The current weather in {city} is {w} degree")

#Extends this project to next level...