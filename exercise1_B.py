#Create a file named exercise1_B.py. In this file a function will be
#created where it will ask the user to insert 2 numbers and the program
#  will tell him which is the largest and which is the smallest. 
# If they are the same, no message will appear
#defining the types of variables
a ,  b = (1,2)
#creating a funtion
def number(a,b):  
    #taking inputs from the user
    #taking the first input as 1st number
    a=int(input("Put the 1st number: "))
    #taking the second input as 1st number
    b=int(input("Put the 2nd number: "))
    #using if condition and accordingly execution
    #if the 1st number is greater than the other
    #  it shows the message of that the 1st number is largest
    #and the other is the smallest
    if(a>b):
        print(str(a) + "" + "is the largest and" + "" + str(b) +"is the smallest")
    #if the 2nd number is greater than the other
    #  it shows the message of that the 2nd number 
    # is largest and other is smallest  
    if(b>a):
        print(str(b) + "" + "is the largest and" + "" + str(a) +"is the smallest")
print(number(a,b))        