# Character Case Checker
# Take a single character from the user and check if it's an uppercase letter, a lowercase letter, or not a letter at all.


character = input("Enter a single character: ")
if character.isupper():
    print("character is an uppercase letter.")
elif character.islower():
    print("character is a lowercase letter.")
else:
     print("character is not a letter.")


    #output
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python character.py
# Enter a single character: a
# character is a lowercase letter.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python character.py
# Enter a single character: A
# character is an uppercase letter.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python character.py
# Enter a single character: 34
# character is not a letter.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>
  