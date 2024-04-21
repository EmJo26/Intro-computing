print ("Python Functions - Activity 3")
#get input from user
n = int(input("Enter a number: ")) 

#define function 
def isPrime(n):
 if n <= 1:                 # 1 and below into negative numbers cannot be prime
    return "Not Prime"
 elif n==2:                 # checking n = 2 then prime 
   return "Prime"                
 else:
  for x in range (2, n):       # division from 2 through to n-1 to check if remainder or not    
    if (n % x == 0):            #checking divisions - if can be divided then not prime
        return "Not Prime"
    if (n % x != 0):            #if cannot be divided then Prime  
         return "Prime"
print (isPrime(n))