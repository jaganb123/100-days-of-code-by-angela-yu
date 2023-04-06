import requests, datetime

params = {
    'lat': 13.058296,
    'lng': 80.175081,
    'formatted': 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=params, )
response.raise_for_status()

data = response.json()
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunset_hour, sunrise_hour)
