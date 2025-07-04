#  Grade Calculator
#  Write a program that takes a student's score (0–100) and prints the corresponding letter grade (A, B, C, D, or F).
score = int(input("Enter the student score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")



    # output
    #  PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python gradecalcu.py
# Enter the student score: 95
# Grade: A
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python gradecalcu.py
# Enter the student score: 87
# Grade: B
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python gradecalcu.py
# Enter the student score: 77
# Grade: C
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python gradecalcu.py
# Enter the student score: 65
# Grade: D
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python> python gradecalcu.py
# Enter the student score: 55
# Grade: F
# PS C:\Users\DHEERAJ KUMAR SAIN\Desktop\python>

