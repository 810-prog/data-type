#   Simple Login System
#   imulate a login system where the user enters a username and password. Print a success message if both are correct, otherwise print an error.

correct_username = "dheeraj"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ") 
if username == correct_username and password == correct_password:
    print("Login successful! Welcome.")
else:
    print("Error: Invalid username or password.") 



    # output
    # PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python login.py
# Enter username: deeraj
# Enter password: 3434
# Error: Invalid username or password.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python login.py
# Enter username: dheeraj
# Enter password: 1234
# Login successful! Welcome.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>

