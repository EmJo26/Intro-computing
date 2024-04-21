#Write a Python program to find the maximum and minimum value of a list.

#Test Data:

#Sample List:

#[25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

#Expected Output:

#Original List: [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

#Maximum value for the above list = 77

#Minimum value for the above list = 14

print ("Python Collections - Activity 3")
myList = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49] #original list given
print ("Original List: ", (myList))             #This will show the original list
myList.sort(reverse=True)                       #This will sort desending with highest number at start
print ("Maximum value for the above list = ", myList[0])    #This will pull the first number which will be the highest as sorted ln20
myList.sort()                                   #This will sort asending so smallest numner at start
print ("Minimum value for the above list = ", myList[0])    #This will pull first number which will be the smallest as sorted ln22
 

