from utilities import DateUtility
import datetime

dateUtil = DateUtility()

#Globals
TODAY = datetime.date.today()
tmp = dateUtil.minMaxDateOfMonth(TODAY)
MONTH_START = tmp[0]
MONTH_END = tmp[1]
#Populate Month Range
MonthData = []
for date in range(MONTH_START, MONTH_END + 1):
    forDate = datetime.date(year=TODAY.year, month=TODAY.month, day=date)
    tmpDict = {'date': forDate,
               'day': dateUtil.weekDay(forDate)}
    MonthData.append(tmpDict)

print(MonthData)


