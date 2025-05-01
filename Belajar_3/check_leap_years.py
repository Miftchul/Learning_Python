year = int(input("Enter a year: "))
# diveded by 100 means century year(ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year" .format(year))
    
# Not divided by 100 means not century year
# year divided by 4 is leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year" .format(year))
    
# if not divided by 400 (century year) and not divided by 4 (not century year)
# year is not a leap year
else:
    print(year, "is not a leap year" .format(year))


