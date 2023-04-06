import json, requests, datetime, smtplib, time

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def percent_calc(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    percent = round((num1 - num2) / num2 * 100, 2)
    return percent


def get_news(topic):
    news_url = "https://newsapi.org/v2/top-headlines"
    news_api_key = "73dd304f54c54e3b80fb8bdc5bc1b81d"
    news_params = {
        "apiKey": news_api_key,
        "q": topic,
        "from": datetime.datetime.today().strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
    }
    response = requests.get(url=news_url, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    news_list = []
    for i in range(0,2):
        news_list.append(news_data['articles'][i])
    return news_list



## STEP 1: Use https://www.alphavantage.co/
api_key = "AALVQE6F8BNJDN8K"
api_url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": api_key,
}

try:
    # check_date = datetime.datetime.today()
    with open("daily_data.json", "r") as file:
        json_data = json.load(file)
    refreshed_date = json_data["Meta Data"]["3. Last Refreshed"]
    # print(check_date, datetime.datetime.strptime(refreshed_date, "%Y-%m-%d"))
except FileNotFoundError:
    with open("daily_data.json", "w") as file:
        json.dump(json_data, file, indent=2)
    response = requests.get(url=api_url, params=params)
    response.raise_for_status()
    json_data = response.json()
finally:
    data_list = []
    i = 0
    send_email = False
    try_date = datetime.datetime.today()
    try_date_str = try_date.strftime("%Y-%m-%d")
    while i < 2:
        key_available = json_data["Time Series (Daily)"].get(try_date_str, False)
        if key_available:
            data_list.append(json_data["Time Series (Daily)"].get(try_date_str, 0))
            i += 1
        try_date = try_date - datetime.timedelta(days=1)
        try_date_str = try_date.strftime("%Y-%m-%d")
    percentage_diff = percent_calc(data_list[0]["4. close"], data_list[1]["4. close"])
    if percentage_diff > 3:
        send_email = True
        news_list = get_news("tesla")



# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com / email
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if send_email:
    my_email = "birthday_wishes1@outlook.com"
    app_password = "ignjjolojotnbvjj"
    server = "outlook.office365.com"
    msg1 = """TSLA: up by 3"""
    msg2 = f"""Headline: {news_list[0]['title']}\nBrief: {news_list[0]['description']}"""
    msg3 = f"""Headline: {news_list[1]['title']}\nBrief: {news_list[1]['description']}"""
    mail_list = [msg1, msg2, msg3]
    # print(mail_list)
    con = smtplib.SMTP(server, port=587)
    con.starttls()
    con.login(user=my_email, password=app_password)
    for i in mail_list:
        print("send message")
        print(f"Subject:alert about {STOCK}\n\n{i}")
        con.sendmail(from_addr=my_email, to_addrs="jagan2221997@gmail.com",
                     msg=f"Subject:alert about {STOCK}\n\n{i}")
        time.sleep(5)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

