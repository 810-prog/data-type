# Evenly Divisible
# Ask the user for a number and check if it's divisible by both 4 and 6.
number = int(input("enter the number : "))
if number % 2 == 0 and number % 4 == 0:
    print("number is divisible by 2 and 4.")
else:
    print ("number is not divisible by 2 and 4")


 # output
#  PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python divisible.py
# enter the number : 24
# number is divisible by 2 and 4.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python divisible.py
# enter the number : 25
# number is not divisible by 2 and 4
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>