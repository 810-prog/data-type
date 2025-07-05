# Leap Year Checker
# Ask the user to input a year and determine whether it is a leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year is a leap year.")
else:
    print("year is not a leap year.")




# # output
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python leap_year.py
# Enter a year: 2000
# year is a leap year.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python leap_year.py
# Enter a year: 2001
# year is not a leap year.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>
