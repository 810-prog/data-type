# Just like break we have another statement, continue,
# which skips the execution of the code after itself and goes back to the start of the loop. 
# That means it will help you to skip a part of the loop. 
# In the below example we will ask the user to input an integer, 
# if the input is negative then we will ask again, if positive then we will square the number.
#  To get out of the infinite loop user must input 0.
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("invalid number ")