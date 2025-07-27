# 1. Print numbers from 1 to 10
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Print even numbers from 2 to 20
print("2. Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# 3. Print odd numbers from 1 to 19
print("3. Odd numbers from 1 to 19:")
for i in range(1, 20, 2):
    print(i, end=" ")
print("\n")

# 4. Sum of first 10 natural numbers
print("4. Sum of first 10 natural numbers:")
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total, "\n")

# 5. Multiplication table of a number (e.g., 5)
print("5. Multiplication table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
print()

# 6. Reverse countdown from 10 to 1
print("6. Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# 7. Print each character in a string
print("7. Characters in 'Python':")
for ch in "Python":
    print(ch, end=" ")
print("\n")

# 8. Print squares of numbers from 1 to 10
print("8. Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(f"{i}^2 = {i*i}")
print()

# 9. Print all elements of a list
print("9. Elements of the list:")
nums = [10, 20, 30, 40, 50]
for num in nums:
    print(num, end=" ")
print("\n")

# 10. Nested for loop - print pattern
print("10. Star Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()

# 11. Reverse a string using for loop
print("11. Reverse of 'Hello':")
text = "Hello"
reversed_text = ""
for ch in text:
    reversed_text = ch + reversed_text
print(reversed_text, "\n")

# 12. Factorial of a number using for loop
print("12. Factorial of 5:")
factorial = 1
for i in range(1, 6):
    factorial *= i
print("Factorial =", factorial, "\n")

# 13. Print ASCII values of characters
print("13. ASCII values of 'ABC':")
for ch in "ABC":
    print(f"{ch} -> {ord(ch)}")
print()

# 14. Print Fibonacci series up to n terms
print("14. Fibonacci Series (10 terms):")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# 15. Find prime numbers from 1 to 50
print("15. Prime numbers from 1 to 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print("\n")


# ...........................................................................................................
# output
# 1. Numbers from 1 to 10: 
  # 1 2 3 4 5 6 7 8 9 10 

# 2. Even numbers from 2 to 20:
  # 2 4 6 8 10 12 14 16 18 20

# 3. Odd numbers from 1 to 19:
  # 1 3 5 7 9 11 13 15 17 19

# 4. Sum of first 10 natural numbers:
  # Sum = 55

# 5. Multiplication table of 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# 6. Countdown from 10 to 1:
 # 10 9 8 7 6 5 4 3 2 1

# 7. Characters in 'Python':
 # P y t h o n

# 8. Squares of numbers from 1 to 10:
# 1^2 = 1
# 2^2 = 4
# 3^2 = 9
# 4^2 = 16
# 5^2 = 25
# 6^2 = 36
# 7^2 = 49
# 8^2 = 64
# 9^2 = 81
# 10^2 = 100

# 9. Elements of the list:
 # 10 20 30 40 50

# 10. Star Pattern:
# *
# **
# ***
# ****
# *****

# 11. Reverse of 'Hello':
 # olleH

# 12. Factorial of 5:
 # Factorial = 120

# 13. ASCII values of 'ABC':
# A -> 65
# B -> 66
# C -> 67

# 14. Fibonacci Series (10 terms):
 # 0 1 1 2 3 5 8 13 21 34

# 15. Prime numbers from 1 to 50:
 # 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
