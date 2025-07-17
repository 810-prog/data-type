

# Length: You can get the length of a string using the len() function.

# my_string = "Hello"
# print( len(my_string) )  # Output: 5
# my_string = "dhee1223aj"
# print(len(my_string))     #output: 10

# Membership: Check if a substring exists in a string using in or not in.

# my_string = "Hello World"
# print("Hello" in my_string)  # Output: True
# print("h" in my_string)  # Output: False
# print("world" in my_string)  #output: false

# String Manipulation / Strings are Immutable
a = "Hello"
a = "pe"+a[:1]
# a = "W" + a[1:]
print( a ) # Wello

# String Methods: Python strings have a variety of built-in methods. Some of the commonly used methods are:
# We use `.` operator to call a method
# upper(): Converts the string to uppercase.

# my_string = "hello123"
# new_string =  my_string.upper()
# print( new_string )  # Output: HELLO123
# print(my_string) # hello123

# lower(): Converts the string to lowercase.

# my_string = "HELLO"
# print(my_string.lower())  # Output: hello

# strip(): Removes leading and trailing whitespaces.

# my_string = "  hello  "
# print(my_string.strip())  # Output: hello

# my_string = "--hel-lo--"
# print(my_string.strip("-"))  # Output: hel-lo

# my_string = "  hello  "
# print(my_string.lstrip())  # Output: hello

# my_string = "  hello  "
# print(my_string.rstrip())  # Output: hello

# replace(old, new): Replaces occurrences of a substring.

# my_string = "Hello World"
# print(my_string.replace("o", "-"))  # Output: Hello Python

# split(): Splits the string into a list based on a delimiter (default is whitespace).

# my_string = "my name is vipin"
# print(my_string.split())  # Output: ['my', 'name', 'is', 'vipin']

# my_string = "15/7/2025"
# print(my_string.split("/"))  # Output: ['15', '7', '2025']

# join(iterable): Joins elements of an iterable (like a list) into a single string, with a specified separator.

# words = ['my', 'name', 'is', 'vipin']
# print("".join(words))  # Output: mynameisvipin
# print(" ".join(words))  # Output: my name is vipin

# words = ['15', '7', '2025']
# print( "-".join(words) )

# find(substring): Returns the index of the first occurrence of a substring (or -1 if not found).

# my_string = "Hello World"
# print(my_string.find("o"))  # Output: 4

# count(substring): Counts occurrences of a substring in the string.

# my_string = "Hello World, Hello Python"
# print(my_string.count("Hello"))  # Output: 2

# username = "lyfofvipin"
# my_string = input("Enter Your Username: ")
# if username.casefold() == my_string.casefold():
#     print("Correct Name")
# else:
#     print("Incorrect Name")

# a = "23sdfsafd"
# print( a.isalnum() )
# int(a)
# if a.isnumeric():
#     int(a)
# else:
#     print("String is not numeric")

# a = "my name is vipin"
# print(a.capitalize())
# print(a.title())

# a = "my name is vipin"
# counter = 0

# while counter < len(a):
#     if counter == 0:
#         print(a[0].upper())
#     else:
#         print(a[counter])
#     counter += 1

