def check_leap_year(year):

 

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

        return "leap year"

    else:

        return "not a leap year"

year = int(input("Enter a year: "))

print(check_leap_year(year))