import random

"""Es defineix una funció que genera un número a l'atzar entre 1 i 100, demana un input l'usuari, si el número es
igual que el generat, imprimeix que l'ha endivinat, si es més petit imprimeix que és més petit i demana un altre
número a l'usuari el númaro inserit prèviament com a màxim.
Fa el mateix si és més gran però després demana un número amb el mínim igual al número anterior
Finalment imprimeix el número generat"""

def atzar():

    numgenerat = random.randrange(1,101)
    numero = int(input("Escriu un número entre 0 i 100\n"))

    if numgenerat == numero:
        print("Molt bé, has endevinat el número")
    elif numero < numgenerat:
        print(f'El número {numero} és més petit'.format(numero = numero))       
        numero = input(f'Escriu un número entre {numero} i 100\n'.format(numero = numero))
        
    else:
        print(f'El número generat és més gran'.format(numero = numero))
        numero = input(f'Escriu un número entre 100 i {numero}\n'.format(numero = numero))
    print(f'El número era {numgenerat}'.format(numgenerat = numgenerat))
    



