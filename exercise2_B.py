#Create a file named exercise2_B.py. In this file, 
# a function will be created where the user will be asked to enter 
# a number and this will indicate whether it is even or odd
#declaring the type of the number 
z=1
#creating the function to check the number entered is even or odd
def evenOrodd(z):
    #taking number as input
    z=int(input("Enter the number: "))
    #using the condition if number is divisible by 2
    if( z%2 == 0):
        #then number is even
        print("The number entered " + str(z) + "" + "is even")
        #oppposingly the number is not divisible by 2
    else:
        #the entered number is odd
        print("The number entered " + str(z) + "" + "is odd")
print(evenOrodd(z))            