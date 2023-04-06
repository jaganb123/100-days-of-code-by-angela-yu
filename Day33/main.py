import requests, smtplib, datetime

MY_LAT = 13.058296
MY_LNG = 80.175081

iss_url = "http://api.open-notify.org/iss-now.json"
sunrise_suset_api = "https://api.sunrise-sunset.org/json"
sunrise_suset_params = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url=iss_url)
response.raise_for_status()

iss_data = response.json()
iss_lat = float(iss_data['iss_position']['latitude'])
iss_lng = float(iss_data['iss_position']['longitude'])
# print(iss_data)
# iss_lat, iss_lng = 13, 80
if (iss_lat - 5) < MY_LAT < (iss_lat + 5) and (iss_lng - 5) < MY_LNG < (iss_lng + 5):
    response = requests.get(url=sunrise_suset_api, params=sunrise_suset_params)
    response.raise_for_status()

    sunrise_set_data = response.json()
    today_sunrise = int(sunrise_set_data['results']['sunrise'].split('T')[1].split(':')[0])
    today_sunset = int(sunrise_set_data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.datetime.utcnow().hour
    # print(sunrise_set_data, today_sunrise, today_sunset, time_now)
    if today_sunset < time_now > today_sunrise:
        print('sending email')
        my_email = "birthday_wishes1@outlook.com"
        password = "AXh9*)f+d1*GQO0"
        app_password = "ignjjolojotnbvjj"
        server = "outlook.office365.com"

        con = smtplib.SMTP(server, port=587)
        con.starttls()
        con.login(user=my_email, password=app_password)
        con.sendmail(from_addr=my_email, to_addrs="jagan2221997@gmail.com", msg="Subject:ISS is above\n\nHi Jagan,\nlook above ISS is passing above your home...")

