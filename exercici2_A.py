"""Es defineix una funció que rep un String de l'usuari, si el String es
troba en la llista donada, imprimeix un format un missatge diferent per cadascún
Si no es troba diu que no està a la llista"""


def elegeixNom():
    myList = ["Oriol","Roger","Carles","Maria","Joan"]

    nom = input(f'Insereix un nom en {myList}\n'.format(myList = myList))

    if nom == myList[0]:
        print(f'Has elegit el nom {myList[0]}'.format(nom = 'Oriol'))
    elif nom == myList[1]:
        print(f'Has elegit el nom {myList[1]}'.format(nom = 'Roger'))
    elif nom == myList[2]:
        print(f'Has elegit el nom {myList[2]}'.format(nom = 'Carles'))
    elif nom == myList[3]:
        print(f'Has elegit el nom {myList[3]}'.format(nom = 'Maria'))
    elif nom == myList[4]:
        print(f'Has elegit el nom {myList[4]}'.format(nom = 'Joan'))
    else:
        print(f'El nom {nom} no està a la llista'.format(nom = nom))
    
        
        