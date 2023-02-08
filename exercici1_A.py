
"""Es defineix una funció que rep 2 números de l'usuari i imprimeix en format 
quin es més gran, quin més petit o si són iguals"""

def maxmin():
    #Cast les entrades per operar amb enters i no Strings
    num1 = int(input("Escriu un número:\n"))
    num2 = int(input("Escriu un número:\n"))

    if num1>num2:
        print(f'{num1} > {num2}'.format(num1=num1,num2=num2))
        
    elif num2>num1:
        print(f'{num1} < {num2}'.format(num1=num1,num2=num2))
    else:
        print(f'{num1} i {num2} Són iguals'.format(num1=num1,num2=num2) )
    