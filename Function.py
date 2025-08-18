def days_in_month():
    month = int(input("Enter the month number (1-12): "))
    year = int(input("Enter the year: "))
    
    if month < 1 or month > 12:
        print("Invalid month number.")
        return

    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("31 days")
    elif month in [4, 6, 9, 11]:
        print("30 days")
    elif month == 2:
        if is_leap_year(year):
            print("29 days (Leap year)")
        else:
            print("28 days")
    else:
        print("Invalid month.")

def is_leap_year(year=None):
    if year is None:
        year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
        return True
    else:
        print(f"{year} is not a leap year.")
        return False

def evenly_divisible():
    num = int(input("Enter a number: "))
    if num % 4 == 0 and num % 6 == 0:
        print(f"{num} is divisible by both 4 and 6.")
    else:
        print(f"{num} is NOT divisible by both 4 and 6.")

def character_case_checker():
    char = input("Enter a single character: ")
    if len(char) != 1:
        print("Please enter exactly one character.")
    elif char.isupper():
        print("Uppercase letter.")
    elif char.islower():
        print("Lowercase letter.")
    elif char.isalpha():
        print("It's a letter but not uppercase or lowercase.")
    else:
        print("Not a letter.")

def time_of_day_greeting():
    hour = int(input("Enter the hour (0-23): "))
    if hour < 0 or hour > 23:
        print("Invalid hour.")
    elif 5 <= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 17:
        print("Good afternoon!")
    elif 17 <= hour < 21:
        print("Good evening!")
    else:
        print("Good night!")

def sum_first_10_natural_numbers():
    total = sum(range(1, 11))
    print(f"Sum of the first 10 natural numbers is: {total}")

def print_even_numbers_2_to_10():
    print("Even numbers from 2 to 10:")
    for i in range(2, 11, 2):
        print(i, end=' ')
    print()

def factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial of {num} is {result}")

def countdown():
    print("Countdown from 10 to 1:")
    for i in range(10, 0, -1):
        print(i, end=' ')
    print()

def sum_of_even_numbers():
    N = int(input("Enter a positive integer N: "))
    total = 0
    i = 1
    while i <= N:
        if i % 2 == 0:
            total += i
        i += 1
    print(f"Sum of even numbers up to {N} is {total}")

def smallest_divisor():
    num = int(input("Enter a number to find its smallest divisor (excluding 1): "))
    if num <= 1:
        print("Enter a number greater than 1.")
        return
    for i in range(2, num + 1):
        if num % i == 0:
            if i == num:
                print(f"{num} is a prime number. Smallest divisor is {num}.")
            else:
                print(f"Smallest divisor of {num} is {i}.")
            break

