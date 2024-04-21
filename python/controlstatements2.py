print("Activity 2")
#Write a Python program that accepts three numbers from the user and prints "Increasing order" if the numbers are in the increasing order, "Decreasing order" if the numbers are in the decreasing order, and "Neither increasing or decreasing order" otherwise.

#Test Data:

#Input first number: 1524
#Input second number: 2345
#Input third number: 3321

#Expected Output :

#Increasing order.

#input from user 3 numbers 
a = int(input("Enter an Integer: "))
print(a)
b = int(input("Enter an Integer: "))
print(b)
c = int(input("Enter an Integer:"))
print (c)
# Ascending order
if a<b<c:
    print("Increasing order")
elif a>b>c:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing order")