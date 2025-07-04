#     Age Category Checker
#     Take the user's age as input and print a message indicating if they are a child, teenager, adult, or senior.

# Age Group Criteria:
# 0–10: Child

# 11–19: Teenager

# 20–35: Adult

# 36 and above: Senior

age = int(input("Enter your age: "))
if age <= 10:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 35:
    print("You are an Adult.")
else:
    print("You are a Senior.")

    # output
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python age.py
# Enter your age: 12
# You are a Teenager.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python age.py
# Enter your age: 10
# You are a Child.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python age.py
# Enter your age: 0
# You are a Child.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python age.py
# Enter your age: 65
# You are a Senior.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python age.py
# Enter your age: 22
# You are an Adult.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>