import calendar

year = int(input("enter year: "))
month = int(input("enter month: "))

cal = calendar.month(year, month)
print(cal)