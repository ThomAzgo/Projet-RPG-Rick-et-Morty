from Description import *
from Interaction import*
from Inventaire import *
from Mouvement import *
from Joueur import *
import tkinter as tk
from Quete import*
from random import*
from Combat import*
from Monstre import*
from Sauvegarde import*
from Menu import*
import os

backpack={
        "potion":["Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins","Potion de Soins"],
        "equipement":[],
        "objetDeQuete":[],
        "argent":"0"
    }

def Game(x,y) :
    os.system("cls")
    varRand=randint(1,4)

    print(' ')
    print(x,y)
    Description(x,y,descriptionMap)
    print(' ')
    print("1 = Intéragir")
    print("2 = Se déplacer")
    print("3 = Ouvrir son inventaire")
    print("4 = Ouvrir la MAP")
    print("5 = Voir la quête en cours")
    print("6 = Vos stats")
    print("7 = Sauvegarder")
    
    joueur = int(input())
    if joueur == 1 :
        if str(x)+","+str(y) in interaction:
            if interaction[str(x)+","+str(y)][4]=="oui":
                Interaction(x,y,backpack)
                Game(x,y)
            else:
                print("Il n'y a pas d'interaction possible ici")
                Game(x,y)
        else:
            print("Il n'y a pas d'interaction possible ici")
            Game(x,y)
    

    elif joueur == 2 :
        print("Vous vous déplacez.")
        m = Mouvement(x,y)
        if varRand==3:
            c=Combat(OrdreDePassage(PickAMonster()))
            if c=="perdu":
                quit()
            AjouterInventaire(backpack,"300","argent")
        Game(m[0],m[1])

    elif joueur == 3:
        test=False
        while test==False:
            print("Vous êtes dans votre sac magique, veuillez choisir l'une des sacoches :")
            print("1 = La sacoche à potions")
            print("2 = La sacoche à équipements")
            print("3 = La sacoche d'objets de quête")
            print("4 = Votre bourse d'argent")
            print("5 = Retour")
            b=int(input())
            test=ParcourirInventaire(backpack,b)
            
        Game(x,y)
    elif joueur == 4:
        fenetre = tk.Tk()
        photo = tk.PhotoImage(file='MapPrologue.png')
        label = tk.Label(fenetre, image=photo)
        label.pack()
        print("FERMER LA MAP AVANT TOUTE AUTRE ACTION OU LE JEU CRASHERA")
        Game(x,y)
        fenetre.mainloop()
    
    elif joueur == 5:
        print(dicoQueteActive["g"])
        Game(x,y)
    
    elif joueur==6:
        VoirStat()
        attendre=input()
        Game(x,y)

    elif joueur==7:
        Save(x,y,backpack)
        Game(x,y)

    
    else : 
        print("Vous avez mal tapé ! Veuillez recommencer.")
        Game(x,y,)




