# Write a function to display Days in a Month
# Ask the user to input a month (1–12) and print how many days are in that month (consider leap year for February).
   
# month = int(input("Enter month (1-12): "))
# year = int(input("Enter year: "))
# def days_in_month(month, year):
#     if month == 2:
#         if (year % 4 == 0):
#             return 29
#         else:
#             return 28
#     elif month in [4, 6, 9, 11]:
#         return 30
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     else: 
#         return "Invalid month"
# print("Days in month:", days_in_month(month, year))
    
                            
# Write a function to display  Leap Year Checker
# Ask the user to input a year and determine whether it is a leap year or not.

# def is_leap_year(year = None):
 
#      if year is None :
#           year = int(input("Enter a year to check leap year: "))
#      if (year % 4 == 0):
#         return "true"
#      else:
#         return "false"
     
# output = is_leap_year()
# print(output)     

 
# Write a function to display Evenly Divisible
# Ask the user for a number and check if it's divisible by both 4 and 6.

# def evenly_divisible():
#  num = int(input("Enter a number: "))
#  if num % 4 == 0 and num % 6 == 0:
#     return "True"
#  else:
#     return "False"
# output = evenly_divisible()
# print(output)

# Write a function to display Character Case Checker
# Take a single character from the user and check if it's an uppercase letter, a lowercase letter, or not a letter at all.

# def character_case_checker(ch):
#     if ch.isupper():
#         return "Uppercase Letter"
#     elif ch.islower():
#         return "Lowercase Letter"
#     elif ch.isdigit():
#         return "It's a Digit"
#     else:
#         return "Not a Letter"
    
# output = character_case_checker("23")
# print(output)
    
# Write a function to display Time of Day Greeting
# Ask the user to enter the time (in hours) and print a greeting based on the time of day:
#     Morning (5 AM - 12 PM)
#     Afternoon (12 PM - 5 PM)
#     Evening (5 PM - 9 PM)
#     Night (9 PM - 5 AM)

# def time_of_day_greeting():
#     hour = int(input("Enter the hour (0-23): "))
#     if hour < 0 or hour > 23:
#         print("Invalid hour.")
#     elif 5 <= hour < 12:
#         print("Good morning!")
#     elif 12 <= hour < 17:
#         print("Good afternoon!")
#     elif 17 <= hour < 21:
#         print("Good evening!")
#     else:
#         print("Good night!")
    
# output = time_of_day_greeting()
# print(output)

# Write a function to display the sum of the first 10 natural numbers.
# def sum_first_10():
#     add = 0
#     for x in range(1, 11):
#         add = add + x
#         print(add)

# sum_first_10()

# Write a function to display print even numbers from 2 to 10.
# def print_even_2_to_10():
#     for x in range(2, 11, 2):
#         print(x, end=" ")
#     print()
# print_even_2_to_10()    

# Write a function to display calculate the factorial of a given number.
# def factorial():
#     num = int(input("Enter a number: "))
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     print(f"Factorial of {num} is {result}")
# factorial()    

# Write a function to display print numbers in a countdown from 10 to 1.
# def countdown():
#     for i in range(10, 0, -1):
#         print(i, end=" ")
#     print()
# countdown()    

# Write a function to display Sum of Even Numbers: 
# Write a program that asks the user to enter a positive integer N. Use a while loop to iterate from 1 up to N. Inside the loop, use an if statement to check if the current number is even. If it is, add it to a running total. Finally, print the sum of all even numbers up to N.
# def sum_of_even_numbers():
#     N = int(input("Enter a positive integer N: "))
#     total = 0
#     i = 1
#     while i <= N:
#         if i % 2 == 0:
#             total += i
#         i += 1
#     print(f"Sum of even numbers up to {N} is {total}")
#     sum_of_even_numbers()

# Write a function to display to find and print the smallest divisor of that number (excluding 1). Use an if-else statement to handle the case where the number itself is prime (its smallest divisor will be itself).
def smallest_divisor(n):
    if n <= 1:
        return "Number should be greater than 1"
    for i in range(2, n + 1):
        if n % i == 0:
            return i
smallest_divisor()        
