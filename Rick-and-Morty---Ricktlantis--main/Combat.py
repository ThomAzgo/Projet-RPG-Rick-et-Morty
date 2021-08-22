from Monstre import *
from Attaques import*
from random import*
from Joueur import*
import os

def OrdreDePassage(monster):
    listePassage=[]
    if Player["caracteristiques"] < monster["caracteristiques"]:
        listePassage.append(monster)
        listePassage.append(Player)
    else :  
        listePassage.append(Player)
        listePassage.append(monster)

    return listePassage
        
def FindSort(sort,lanceur,cible):
    if sort=="Doliprane mk1  Soins basique coûte 20 d'endurance":
        Soin(lanceur,lanceur)
    elif sort=="Armor Breaker 3003  Réduit l'armure coûte 50 endurance":
        Corrosif(lanceur,cible)
    elif sort=="Turbo Flemme  Réduit l'endurance de l'ennemi coûte 30 d'enrucance":
        Fatigue(lanceur,cible)
    elif sort=="Dopage douteux Boost d'attaque coûte 30 d'enrucance":
        BoostAttaque(lanceur,lanceur)
    elif sort=="Rick-cola  Boost de def coûte 30 d'enrucance":
        BoostDefense(lanceur,lanceur)
    elif sort=="Méga-Sangsue  Drain de vie sur la cible coûte 40 d'endurance":
        VolDeVie(lanceur,lanceur)
    elif sort=="Google Glass v69420  Permet de voir les stats de la cible coûte 30 d'endurance pour une cible unique et 60 pour voir les tiennes plus celles du monstre":
        Clairevoyance(lanceur,cible)
    elif sort=="Doliprane mk2  Soins supérieur coûte 40 d'endurance":
        SoinSuperieur(lanceur,lanceur)
    elif sort == "X Æ A-12  Reset tes stats à 0":
        RemiseAzero(lanceur,lanceur)
    elif sort == "Rick-cola Zero  Boost de def supérieur coûte 60 d'endurance":
        BoostDefenseSup(lanceur,lanceur)
    elif sort == "Nanorobots 5G  Boost d'endurance possible si on est en dessous de 30 d'endurance":
        BoostEndurance(lanceur,lanceur)
    elif sort=="Reformatage USB :Reset toutes les stats de l'ennemi sauf les pv":
        SortErrosion(lanceur,lanceur)
    elif sort == "Picole":
        Picole(lanceur)
    elif sort == "Gueule de Bois":
        GueuleDeBois(lanceur)
    elif Molotov == "Molotov":
        Molotov(lanceur,cible)
    elif PacteDeSang == "Pacte de Sang":
        PacteDeSang(lanceur,lanceur)
    elif MorsureSauvage == "Morsure Sauvage":
        MorsureSauvage(lanceur,cible)
    elif DesJetees == "Dés Jetés":
        DesJetees(lanceur,cible)
    elif NeverGonnaGiveYouUp == "Never Gonna Give You Up":
        NeverGonnaGiveYouUp(lanceur,lanceur)

    
    
  

    

def Combat(liste):
    encour=True # On dit que le combat est en cours
    i=0
    os.system("cls")
    print("Vous avez engé un combat !")
    print(liste[0]["classe"])
    print(liste[1]["classe"])
    attendre=input()
    while  encour==True:   #Tant que le combat est en cours la boucle s'execute   
        rand=randint(2,3)    
       
        if liste[i]["classe"]=="Morty" or liste[i]["classe"]=="Rick": # si c'est le tour du joueur
            print("C'est votre tour de combat que souhaitez vous faire ?")
            print("1=Attaque Basique")
            print("2=Attaque Spéciale")
            choix=int(input())
            
                
            if choix==1:
                if i==0:
                    AttaquePhysique(liste[0],liste[1])
                    print("Vous lancez une attaque 1")
                    print(liste[1]["carac2"][1])
                    i=i+1
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ GAGNÉ")
                        return "gagner"
                else:
                    AttaquePhysique(liste[1],liste[0])
                    print("Vous lancez une attaque 2")
                    print(liste[0]["carac2"][1])
                    i=i+1
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ GAGNÉ")
                        return "gagner"

            elif choix==2:
                if i==0:
                    g=0
                    while g<len(liste[0]["Sort"]):
                        print(str(g)+":"+liste[0]["Sort"][g]) 
                        g=g+1
                    choix2=int(input())
                    FindSort(liste[0]["Sort"][choix2],liste[0],liste[1])
                    print(liste[0]["carac2"][1])
                    i=i+1
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ GAGNÉ")
                        return "gagner"
                else:
                    g=0
                    while g<len(liste[1]["Sort"]):
                        print(str(g)+":"+liste[1]["Sort"][g]) 
                        g=g+1
                    choix2=int(input())
                    FindSort(liste[1]["Sort"][choix2],liste[1],liste[0])
                    print(liste[1]["carac2"][1])
                    i=i+1
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ GAGNÉ")
                        return "gagner"
                
            

        else : # Sinon c'est le tour de l'ennemi
            print("Tour de l'ennemi")
            if i==0:
                
                
                if rand==2:
                    print("L'ennemi vous attaque")
                    AttaquePhysique(liste[0],liste[1])
                    print("Il vous reste : "+str(liste[1]["carac2"][1]))
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ PERDU")
                        return "perdu"
                    i=i+1
                else:
                    rand=randint(0,len(liste[0]["Sort"])-1)
                    print("L'ennemi vous attaque")
                    FindSort(liste[0]["Sort"][rand],liste[0],liste[1])
                    print("Il vous reste : "+str(liste[1]["carac2"][1]))
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ PERDU")
                        return "perdu"
                    i=i+1

                
                    
                
        
                
            elif i==1:
                    
                if rand==2:
                    print("L'ennemi vous attaque")
                    AttaquePhysique(liste[1],liste[0])
                    print("Il vous reste : "+str(liste[0]["carac2"][1]))
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ PERDU")
                        return "perdu"
                    i=i+1
                        
                else:
                    rand=randint(0,len(liste[0]["Sort"])-1)
                    print("L'ennemi vous attaque")
                    FindSort(liste[1]["Sort"][rand],liste[1],liste[0])
                    print("Il vous reste : "+str(liste[0]["carac2"][1]))
                    if liste[0]["carac2"][1]<=0 or liste[1]["carac2"][1]<=0: #Liste contient le Player ou le monstre en fonction de l'orde. SI les pv de l'un des deux tombe à 0 alors le combat prend fin
                        encour=False
                        print("Combat Finit")
                        print("VOUS AVEZ PERDU")
                        return "perdu"
                    i=i+1

                
                
                

            



        

        if i==2: #Rénitialisé le conteur de tours
            i=0


    


    