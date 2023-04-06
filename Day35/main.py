import requests, json
import os
import smtplib
import datetime
api_key = os.environ.get("OWM_API_KEY")
#"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}"
api_url = "https://api.openweathermap.org/data/3.0/onecall"
latitude = 13.058382
longitude = 80.175166


params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

try:
    with open("OWM.json") as file:
        weather_data = json.load(file)
    data_time = datetime.datetime.fromtimestamp(weather_data['hourly'][0]['dt'])
    time_delta = data_time - datetime.datetime.now()
    # data_time.hour
    print(data_time.hour, datetime.datetime.now().hour, time_delta.seconds/60)
    # raise FileNotFoundError
except FileNotFoundError:
    response = requests.get(url=api_url, params=params)
    response.raise_for_status()
    weather_data = response.json()
    with open("OWM.json", "w") as file:
        json.dump(weather_data, file, indent=2)


weather_slice = weather_data["hourly"][:12]
will_rain = False
for i in [x['weather'][0]['id'] for x in weather_slice]:
    if i <= 700:
        will_rain = True
if will_rain:
    my_email = "birthday_wishes1@outlook.com"
    password = os.environ.get("EMAIL_PASS")
    app_password = os.environ.get("EMAIL_APP_PASS")
    server = "outlook.office365.com"

    # con = smtplib.SMTP(host=server, port=587)
    # con.starttls()
    # con.login(user=my_email, password=app_password)
    # con.sendmail(from_addr=my_email, to_addrs="jagan2221997@gmail.com",
    #              msg="Subject:It's gonna rain today\n\nHi Jagan,\n\tlooks like it's gonna rain today,"
    #                  "\nbring your umbrella.")
