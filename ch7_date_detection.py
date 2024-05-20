import re

months_30 = (4, 6, 9, 11)

date_regex = re.compile(r'(\d?\d)/(\d?\d)/(\d\d\d\d)')
mo = date_regex.search('this is a date: 29/2/2024')

print(mo.group())
day = mo.group(1)
month = mo.group(2)
year = mo.group(3)

if len(day) < 2:
    day = day.zfill(2)
if len(month) < 2:
    month = month.zfill(2)

if int(month) == 2:
    if int(year)%4 == 0:
        if int(year)%100 == 0 and int(year)%400 != 0:
            print('is not leap year')
            leap_year = 0
        else:
            print('Is leap year')
            leap_year = 1
    else:
        print('Is not leap year')
        leap_year = 0

if int(day) > 31  or int(day) < 1:
    print('Invalid day')
if int(month) > 12 or int(month) < 1:
    print('Invalid month')
if int(year) > 2999 or int(year) < 1000:
    print('Invalid year')

if int(month) in months_30 and int(day) > 30:
    print('Invalid date (month has 30 days)')
if int(month) == 2:
    if leap_year == 0 and int(day) > 28:
        print('Invalid date (month has 28 days)')
    if leap_year == 1 and int(day) > 29:
        print('Invalid date (month has 29 days)')
