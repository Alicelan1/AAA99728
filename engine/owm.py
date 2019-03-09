import requests

def OWM_lat_lon(lat,lon):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?appid=a54737c8c1da3e8bbde5e1b9a57f4b63&lat=' + str(lat) + '&lon=' + str(lon) + '&lang=zh_tw&units=metric').json()
    weather = str(r['weather'][0]['description'])
    temperature = str(r['main']['temp'])
    temperatureMin = str(r['main']['temp_min'])
    temperatureMax = str(r['main']['temp_max'])
    wind = str(r['wind']['speed'])
    location = str(r['name'])
    content = "所在地：" + location + "\n天氣狀況：" + weather + "\n溫度：" + temperature + "\n最高溫：" + temperatureMax + "\n最低溫：" + temperatureMin+"\n風速：" + wind
    return content
