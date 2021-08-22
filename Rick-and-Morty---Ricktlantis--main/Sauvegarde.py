from Game import*
from Interaction import*
from Description import*
from Quete import*
def Save(x,y,backpack):
    ########## Save du Player ###############
    fichierPlayer = open("player.txt", "w") # On ouvre le fichier player.txt qui va contenir tout le dico
    for key, data in Player.items() : # Pour chaque clées dans le dico mais aussi pour chaque data
        fichierPlayer.write(key)       #on écrit la clef
        fichierPlayer.write(':')        # un séparateur ":"
        fichierPlayer.write(str(data)+'\n') # et ensuite la date convertie en string, on concatene avec "\n" qui permet un saut à la ligne   
    fichierPlayer.close() #ON OUBLIE PAS DE FERMER LE FICHIER
    ########## Fin de Save Player ############


    ########## Save de Description ###########
    fichierDescription = open("description.txt", "w")
    for key, data in descriptionMap.items():
        fichierDescription.write(key)
        fichierDescription.write(":")
        fichierDescription.write(str(data)+'\n')
    fichierDescription.close()
    ########## Fin de Save Desription #########


    ########## Save de Backpack ###############
    fichierBackpack = open("backpack.txt", "w")
    for key, data in backpack.items():
        fichierBackpack.write(key)
        fichierBackpack.write(":")
        fichierBackpack.write(str(data)+'\n')
    fichierBackpack.close()
    ########## Fin de Save Backpack ##########


    ########## Save de Mouvement #############
    fichierMouvement = open("mouvement.txt", "w")
    fichierMouvement.write(str(x)+'\n')
    fichierMouvement.write(str(y))
    fichierMouvement.close()
    ########## Fin de Save Mouvement #########


    ########## Save de Interaction ###########
    fichierInteraction = open("interaction.txt", "w")
    for key, data in interaction.items() :
        fichierInteraction.write(key)
        fichierInteraction.write(":")
        fichierInteraction.write(str(data)+'\n')
    fichierInteraction.close()
    ########## Fin de Save Interaction ######


    ########## Save de QueteActive ###########
    fichierQueteActive = open("queteActive.txt", "w")
    for key, data in dicoQueteActive.items() :
        fichierQueteActive.write(key)
        fichierQueteActive.write(":")
        fichierQueteActive.write(str(data)+'\n')
    fichierQueteActive.close()
    ########## Fin de Save QueteActive #######


    ########## Save de QuetePasActive ########
    fichierQuetePasActive = open("quetePasActive.txt", "w")
    for key, data in dicoQuetePasActive.items() :
        fichierQuetePasActive.write(key)
        fichierQuetePasActive.write(":")
        fichierQuetePasActive.write(str(data)+'\n')
    fichierQuetePasActive.close()
    ########## Fin de Save QuetePasActive ####


    ########## Save de Objet #################
    fichierObjet = open("objet.txt", "w")
    for key, data in dicoObj.items():
        fichierObjet.write(key)
        fichierObjet.write(':')
        fichierObjet.write(str(data)+'\n')
    fichierObjet.close()
    ########## Fin de Save Objet #############


def Load(backpack):
    ########## Load de Player #################
    fichierPlayer = open("player.txt", "r") # On ouvre le fichier player.txt ou est contenu tout le dico
    line = fichierPlayer.readlines()# "line"est la variable qui va contenir chaque ligne contenue dans player.txt
    for lines in line: # Ici on fait un for pour chaque "lines" dans "line"
        element2 = lines.split(':') # .split permet de divier en 2 partie un grâce à un séparateur ici ":" en  une liste appelé element2
        cle = element2[0] # à l'indice 0 d'element2 on a ce qui était à gauche de ":" c'est à dire les clés 
        data = element2[1] #à l'indice 1 d'element2 on a ce qui était à droite de ":" c'est à dire la data
        data = data.replace('\n','') # \n est un résidu car lorsque l'on saute une ligne dans un fichier on a automatiquement donc avec .replace on remplace les '\n' par rien ''
        if cle == "classe": # ici la classe étant le seul élément n'étant pas une liste il faut faire la distinction avec les listes
           Player[cle] = data # on remplace donc l'élément 
        else: # Sinon on aura forcement à faire à une liste
            Player[cle] = eval(data) # eval() permet de remplacer literalement par ce que le string signifie exemple : eval("2+2") nous donnera 4 en résultat
                                     # Dans notre cas on remplace data="[1,2,"Texte"]" par data=[1,2,,"Texte"]
    fichierPlayer.close()#ON OUBLIE PAS DE FERMER LE FICHIER
    ########## Fin de Load Player #############


    ########## Load de Description ############
    fichierDescription = open("description.txt", "r")
    line = fichierDescription.readlines()
    for lines in line:
        element2 = lines.split(":")
        cle = element2[0]
        data = element2[1]
        data = data.replace('\n','')
        descriptionMap[cle] = eval(data)

    fichierDescription.close()
    ########## Fin de Load Description ########
    

    ########## Load de Backpack ###############
    fichierBackpack = open("backpack.txt", "r")
    line = fichierBackpack.readlines()
    for lines in line:
        element2 = lines.split(":")
        cle = element2[0]
        data = element2[1]
        data = data.replace("\n","")
        backpack[cle] = eval(data)
    fichierBackpack.close()
    ########## Fin de Load Backpack ##########
    

    ########## Load de Mouvement #############
    fichierMouvement = open("mouvement.txt", "r")
    ligne = fichierMouvement.readline()
    x = int(ligne)
    ligne = fichierMouvement.readline()
    y = int(ligne)
    fichierMouvement.close()
    ########## Fin de Load Mouvement #########


    ########## Load de Interaction ###########
    fichierInteraction = open("interaction.txt", "r")
    line = fichierInteraction.readlines()
    for lines in line:
        element = lines.split(':')
        cle = element[0]
        data = element[1]
        data = data.replace('\n', '')
        interaction[cle] = eval(data)
    fichierInteraction.close()
    
    ########## Fin de Load Interaction #######


    ########## Load de QueteActive ###########
    fichierQueteActive = open("queteActive.txt", "r")
    line = fichierQueteActive.readlines()
    for lines in line:
        element = lines.split(':')
        cle = element[0]
        data = element[1]
        data = data.replace('\n', '')
        if cle=="g":
            dicoQueteActive[cle] = data
        else :
            dicoQueteActive[cle] = eval(data)
    fichierQueteActive.close()
    
    ########## Fin de Load QueteActive #######


    ########## Load de QuetePasActive ########
    fichierQuetePasActive = open("quetePasActive.txt", "r")
    line = fichierQuetePasActive.readlines()
    for lines in line:
        element = lines.split(':')
        cle = element[0]
        data = element[1]
        data = data.replace('\n', '')
        dicoQuetePasActive[cle] = eval(data)
    fichierQuetePasActive.close()
    ########## Fin de Load QuetePasActive ####


    ########## Load de Objet #################
    fichierObjet = open("objet.txt", "r")
    line = fichierObjet.readlines()
    for lines in line:
        element = lines.split(':')
        cle = element[0]
        data = element[1]
        data = data.replace('\n', "")
        dicoObj[cle] = eval(data)
    fichierObjet.close()
    ########## Fin de Load Objet #############"""
    return x,y