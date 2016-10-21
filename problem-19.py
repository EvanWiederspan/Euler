def getMonthLength(month, year):
    if month == 1:
        if isLeapYear(year):
            return 29
        else:
            return 28
    elif month in [4,6,8,10]:
        return 30
    else:
        return 31

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = 1901 # 1901
month = 0 # january
day = 1 #sunday is 0, were starting on a monday
num = 0 # sunday counter, final answer

while year < 2001:
    day += getMonthLength(month, year) % 7
    day = day % 7
    if day == 0:
        num = num + 1
    month = month + 1
    if (month > 11):
        month = 0
        year = year + 1
print(num)