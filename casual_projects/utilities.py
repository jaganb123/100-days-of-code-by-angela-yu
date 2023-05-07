import datetime

class DateUtility():
    def __init__(self) -> None:
        return None

    def minMaxDateOfMonth(self, date :datetime.date):
            if date.month == 2:
                if not date.year % 4:
                    if not date.year % 100:
                        return (1, 29)
                    else:
                        if not date.year % 400:
                            return (1, 29)
                        else:
                            return (1, 29)
                else:
                    return (1, 28)
            elif date.month in [1, 3, 5, 7, 8, 10, 12]:
                return (1, 31)
            else:
                return (1, 30)
    
    def weekDay(self, date :datetime.date):
        day = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday',
        }
        return day[date.weekday()]
