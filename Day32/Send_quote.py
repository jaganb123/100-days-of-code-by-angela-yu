import smtplib, datetime, random

my_email = "birthday_wishes1@outlook.com"
password = "AXh9*)f+d1*GQO0"
app_password = "ignjjolojotnbvjj"
server = "outlook.office365.com"

con = smtplib.SMTP(server, port=587)
con.starttls()
con.login(user=my_email, password=app_password)

if datetime.datetime.now().weekday() == 2:
    with open("quotes.txt", "r") as quote:
        data = random.choice(quote.readlines())
        today_quote = data.split(sep='\n')[0]
    con.sendmail(from_addr=my_email, to_addrs="jagan2221997@gmail.com", msg=f"Subject:Today's quote\n\n{today_quote}")

