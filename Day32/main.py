##################### Extra Hard Starting Project ######################
import smtplib, pandas, os, datetime, random


def send_email(to_mail, message):
    my_email = "birthday_wishes1@outlook.com"
    # password = "AXh9*)f+d1*GQO0"
    app_password = "ignjjolojotnbvjj"
    server = "outlook.office365.com"
    con = smtplib.SMTP(server, port=587)
    con.starttls()
    con.login(user=my_email, password=app_password)
    con.sendmail(from_addr=my_email, to_addrs=to_mail, msg=f"Subject:Bitrhday Wish\n\n{message}")
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv("birthdays.csv")
today = datetime.datetime.now()
for (index, row) in df.iterrows():
    if (today.month == row.month) and (today.day == row.day):

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'letter_templates/{random.choice(os.listdir("letter_templates"))}') as letter:
            message = letter.read()
        message = message.replace('[NAME]', row['name'])
        message = message.replace('Angela', 'Jagan Babu')
        # 4. Send the letter generated in step 3 to that person's email address.
        send_email(to_mail=row.email, message=message)





