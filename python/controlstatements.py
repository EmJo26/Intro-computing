# Activity 1
#Write a Python program that accepts three numbers and prints "All numbers are equal" if all three numbers are equal, "All numbers are different" if all three numbers are different and "Neither all are equal or different" otherwise.

#Test Data:

#Input first number: 2
#Input second number: 3
#Input third number: 4

#Expected Output :

#All numbers are different.

# input from user
a = int(input("Enter an Integer: "))
print(a)
b = int(input("Enter an Integer: "))
print(b)
c = int(input("Enter an Integer:"))
print (c)
if a==b and a==c: # all numbers are the same 
 print ("All numbers are equal")
else: #if any number is different
 print("All numbers are different")
 
 
 
 
 
