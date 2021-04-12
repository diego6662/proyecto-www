import requests


def temperature():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=763041,co&appid=dfa2f824fc036ff5f2f9c022f70c4a7c')
    json_object = r.json()
    format_add = json_object['weather', 'main']
    print(format_add)
    print('hola')

temperature()


