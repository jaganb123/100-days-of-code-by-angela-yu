import datetime

def generate_month_calender():
    today = datetime.date.today()
    month = today.month
    day = 1
    date_list = []
    try:
        while True:
            date_list.append((today.replace(day=day).isoweekday(), today.replace(day=day)))
            day += 1
    except ValueError:
        return tuple(date_list)
