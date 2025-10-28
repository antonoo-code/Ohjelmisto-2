import json
import requests


paikkakunta = input('Syötä paikkakunta: ')
pyyntö1 = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=5&appid=903dead6282626bee8f141026c21b7cf"
vastaus1 = requests.get(pyyntö1).json()
pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={vastaus1[0]['lat']}&lon={vastaus1[0]['lon']}&appid=903dead6282626bee8f141026c21b7cf"

vastaus2 = requests.get(pyyntö2).json()

temp_celcius = vastaus2['main']['temp']-273.15 
print(f'Paikkakunnalla {paikkakunta} on :{temp_celcius:.2f} celsius astetta.')


