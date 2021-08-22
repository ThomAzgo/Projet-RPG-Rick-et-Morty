from Description import *
from Quete import *
from Game import *

interaction = {

    "3,0":["1=Combatre","2=Fuir","BOUHHYAAAAAAAA","1","oui"],
    "-3,0":["1=Combatre","2=Fuir","BOUHHYAAAAAAAA","3","non"],
    "0,2":["1=Parler au garde","2=Ne rien faire","Rick Garde  Il y a UN PU***N DE MONSTRE. TIENT PREND MON ARME JE ME CASSE D ICI","666","oui"],
    "0,4":["1=Combatre","2=Fuir","BOUHHYAAAAAAAA","2","non"],
    "0,-2":["1=Démarrer le vaisseau","2=Ne rien faire","LETS GO","4","non"],
    "-1,1":["1= Le prendre","2= Ne rien faire","Le regarder partir fièrement","555","oui"],
    "1,1":["1= Ramasser","2= Ne rien faire","Vous ramassez l'objet","444","oui"],
    "1,-1":["1= Accepter","2 = Ne rien faire","Vous lui expliquez la situation et acceptez sa requête","333","oui"]

}



def Interaction(x,y,backpack):
    if descriptionMap[str(x)+","+str(y)][2]==False:
        print(interaction[str(x)+","+str(y)][0])
        print(interaction[str(x)+","+str(y)][1])
        
        choixInteraction = int(input())

        if choixInteraction == 1:
            b=VerfifCondition(str(x),str(y),interaction[str(x)+","+str(y)][3],backpack,interaction)
            
            if b[0]=="rien" and b[1]==True:
                interaction[dicoQueteActive[b[0]][2]+","+dicoQueteActive[b[0]][3]][4]="oui"
            elif b[0]=="rien"and b[1]=="rien":
                pass
                

        elif choixInteraction == 2:
            pass
        else:
            print("Erreur : Veuillez choisir entre 1 et 2.")

    elif descriptionMap[str(x)+","+str(y)]==True:
        pass

