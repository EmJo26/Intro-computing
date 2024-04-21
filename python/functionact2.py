print("Python Functions - Activity 2")

#Write a Python function to calculate the factorial of a number (a non-negative integer n ). The function accepts the number as an argument.

#define function, check n < 0 so need if and else statements? then continuous loop until n is reached.

def factorial (n):          #function name
    if n == 0:              #The factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.
        return 1
    if n <= -1:             # in case anyone puts in a negative number       
        return "not defined for negative numbers"
    else:                   # all other positive numbers
        return n * factorial (n-1)
#ask input from user
n = int(input("Enter a positive number: "))     

print(n,"! = ", factorial(n))    # will display the number inputted and ! for factorials