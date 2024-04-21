print ("Python Functions - Activity 1")

#Write 2 Python functions to: 

#show the list content. 
#find the max value in the list.
#Sample List : [10, 2, 3, 4, 7]

#Expected Output :

#The content of the list is: [10, 2, 3, 4, 7]

#The max value in the list: 10

def my_function():
    print("The content of the list is ", list) # this will show the list
 
list = [10, 2, 3, 4, 7]
    
my_function() 

def my_function(max_list):
    print("The max value in the list: ", max(list)) #this will display the max from the list

max_list = max(list)                                #this is required to get max
my_function(max_list)



