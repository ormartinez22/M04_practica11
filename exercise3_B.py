#defining agr and income type variables
age,income = 1 , 2
#creating the function to take the age and income from the user
def personalData(age,income):
    #taking age as input from the user
    age=int(input("Enter your age: "))
    #requesting to add the income by the user
    income=int(input("Enter your income: "))
    #providing condition if  the person is an adult and is mandatory to pay the tax
    if(age>=18 and income>1200):
        #showing message to pay tax if and only if both the conditions are met
        print("It is necessary that you make the tax return")
    #providing condition if  the person is not an adult and is mandatory or not to pay the tax    
    else:
        #showing message not to pay tax if neither of both the conditions are met
        print("You still cannot make the declaration")
print(personalData(age,income))            