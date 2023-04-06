import smtplib

my_email = "birthday_wishes1@outlook.com"
password = "AXh9*)f+d1*GQO0"
app_password = "ignjjolojotnbvjj"
server = "outlook.office365.com"

con = smtplib.SMTP(server, port=587)
# con.set_debuglevel(True)
# print('connected')
con.starttls()
# print("tls enabled")
con.login(user=my_email, password=app_password)
# print("login loaded")
con.sendmail(from_addr=my_email, to_addrs="jagan2221997@gmail.com", msg="Subject:Birthday Wish\n\nHello Email")
# print('mail sent')
con.close()
