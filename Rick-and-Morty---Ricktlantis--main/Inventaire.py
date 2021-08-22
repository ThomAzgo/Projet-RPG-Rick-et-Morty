from Utiliser import *
from Joueur import*
from Equipement import*

def ParcourirInventaire(backpack,choix):
    i=0
    if choix==1 :
        while i<len(backpack["potion"]):
            print(backpack["potion"][i])
            i=i+1

        print("1 -Utiliser")
        print("2 - Retour")
        choice=int(input())
        print("Rentrer l'item que vous voulez utiliser")
        if choice==1:
            objet = input()
            Utiliser(objet)
            RetirerInventaire(backpack,objet,"potion")
            return False

        elif choice ==2:
            return True
        else :
            ParcourirInventaire(backpack,choix)

   
    if choix ==2 :
        while i<len(backpack["equipement"]):
            print(backpack["equipement"][i])
            i=i+1

        print("1 -Utiliser")
        print("2 - Retour")
        choice=int(input())
        print("Rentrer l'item que vous voulez utiliser")
        
        if choice==1:
            objet = input()
            Equiper(Player,objet)
            RetirerInventaire(backpack,objet,"equipement")
            return False
        elif choice ==2:
            return True
        else :
            ParcourirInventaire(backpack,choix)
     
    if choix ==3:
        while i<len(backpack["objetDeQuete"]):
            print(backpack["objetDeQuete"][i])
            i=i+1

        print("1 -Utiliser")
        print("2 - Retour")
        choice=int(input())
        print("Rentrer l'item que vous voulez utiliser")
        if choice==1:
            print("Utiliser")
            return False
        elif choice ==2:
            return True
        else :
            ParcourirInventaire(backpack,choix)
    
    if choix ==4:
        while i<len(backpack["argent"]):
            print(backpack["argent"][i])
            i=i+1

        print("1 -Utiliser")
        print("2 - Retour")
        print("Rentrer l'item que vous voulez utiliser")
        choice=int(input())
        if choice==1:
            print("Utiliser")
            return False
        elif choice ==2:
            return True
        else :
            ParcourirInventaire(backpack,choix)

    if choix==5:
        return True


def AjouterInventaire(backpack,objet,endroit):
    
    if endroit == "argent":
        backpack["argent"]=int(backpack["argent"])+int(objet)
        backpack["argent"]=str(backpack["argent"])
    else :
        backpack[endroit].append(objet)
    return backpack

def RetirerInventaire(backpack,objet,endroit):
    backpack[endroit].remove(objet)   
    return backpack

def Recompenses(x,y):
    if x==3 and y==1:
        AjouterInventaire(backpack,"Sandales chaussettes","equipement")




