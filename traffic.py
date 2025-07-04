# Traffic Light Instructions
# Ask the user to enter a traffic light color (red, yellow, or green). Print what action to take based on the color. If the color is invalid, print an error message.
color = input("Enter a traffic light color (red, yellow, or green): ")
if color == "red":
    print("STOP.")
elif color == "yellow":
    print("ready to stop.")
elif color == "green":
    print("GO The way is clear.")
else:
    print("Error: Invalid traffic light color.")


    # output

#  PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python traffic.py
# Enter a traffic light color (red, yellow, or green): red
# STOP.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python traffic.py
# Enter a traffic light color (red, yellow, or green): yellow
# ready to stop.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python traffic.py
# Enter a traffic light color (red, yellow, or green): green
# GO The way is clear.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python traffic.py
# Enter a traffic light color (red, yellow, or green): black
# Error: Invalid traffic light color.
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>   