from random import *

Player = {
    "lvl" : [1,0],
    "equipement" : [[0,0,0,0,0,False,"casque"],[0,0,0,0,0,False,"armure"],[0,0,0,0,0,False,"pantalon"],[0,0,0,0,0,False,"bottes"],[0,0,0,0,0,False,"armes"]], #Casque,Armure,Pantalon,Bottes,Arme
    "classe":"Larbin",
    "caracteristiques":[3,75,10,3,100], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[3,75,10,50,100]
}

Monstre = {
    "classe":"Chien",
    "caracteristiques":[3,75,10,3,100], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[3,75,10,50,100]
}
################### Possédé par tout les combattants ###################
def AttaquePhysique(lanceur,cible):
    print("Attaque Physique lancé!")
    coupcrit = randint(0,10)
    if coupcrit == 10:
        PV_perdu = 40 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100 #La variable PV_perdu calcule les PV perdus en prenant en compte l'attaque du lanceur et la défense de la cible.
        print("Coup critique!")
    else:
        PV_perdu = 10 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100
    PV_perdu=int(PV_perdu)
    cible["carac2"][1] = cible["carac2"][1] - PV_perdu
    print("La cible perd "+str(PV_perdu)+ " PV")

################### Sorts des joueurs ###################
def Soin(lanceur,cible):
    if lanceur["carac2"][4] > 20:
        print("Sort de Soin lancé! Coût de 20 d'endurance")
        PV_gagne = 10 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100 #Même calcul que pour l'attaque pour équilibré les soins reçus.
        PV_gagne=int(PV_gagne)
        cible["carac2"][1] = cible["carac2"][1] + PV_gagne
        if cible["carac2"][1] >= cible["caracteristiques"][1]:
            cible["carac2"][1] = cible["caracteristiques"][1]
        lanceur["carac2"][4] = lanceur["carac2"][4] - 20
        print("Le lanceur récupère " +str(PV_gagne)+ " PV")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def SoinSuperieur(lanceur,cible):
    if lanceur["carac2"][4] > 40:
        print("Sort de Soin Supérieur lancé! Coût de 40 d'endurance")
        PV_gagne = 30 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100
        PV_gagne=int(PV_gagne)
        cible["carac2"][1] = cible["carac2"][1] +PV_gagne
        if cible["carac2"][1] >= cible["caracteristiques"][1]:
            cible["carac2"][1] = cible["caracteristiques"][1]
        lanceur["carac2"][4] = lanceur["carac2"][4] - 40
        print("Le lanceur récupère " +str(PV_gagne)+ " PV")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def VolDeVie(lanceur,cible):
    if lanceur["carac2"][4] > 40:
        print("Vol de Vie lancé! Coût de 40 d'endurance")
        PV_perdu = 80 * (10 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100)/100
        PV_perdu=int(PV_perdu)
        cible["carac2"][1] = cible["carac2"][1] - PV_perdu
        PV_gagne = PV_perdu - (20 * PV_perdu/100)
        PV_gagne=int(PV_gagne)
        lanceur["carac2"][1] = lanceur["carac2"][1] + PV_gagne
        if lanceur["carac2"][1] >= lanceur["caracteristiques"][1]:
            lanceur["carac2"][1] = lanceur["caracteristiques"][1]
        lanceur["carac2"][4] = lanceur["carac2"][4] - 40
        print("La cible perd "+str(PV_perdu)+ " PV")
        print("Le lanceur récupère " +str(PV_gagne)+ " PV")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def BoostEndurance(lanceur,cible):
    if lanceur["carac2"][4] < 30:
        print("Boost d'endurance lancé!")
        Endurance_gagne = lanceur["carac2"][4]/2
        Endurance_gagne= int(Endurance_gagne)
        lanceur["carac2"][4] = lanceur["carac2"][4] + Endurance_gagne
        print("Vous récupérez 50% de votre endurance")
    else:
        print("Le sort à échoué ... vous avez TROP d'endurance! (oui vraiment)")

def Corrosif(lanceur,cible):
    if lanceur["carac2"][4] > 50:
        print("Sort de corrosion lancé! Coût de 50 d'endurance")
        Armure_perdu = cible["carac2"][3]/4
        Armure_perdu=int(Armure_perdu)
        cible["carac2"][3] = cible["carac2"][3] - Armure_perdu
        lanceur["carac2"][4] = lanceur["carac2"][4] - 50
        print("La cible perd 25% de son armure")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def Fatigue(lanceur,cible):
    if lanceur["carac2"][4] > 30:
        print("Sort de fatigue lancé! Coût de 40 d'endurance")
        Endurance_perdu = cible["carac2"][4]/2
        Endurance_perdu=int(Endurance_perdu)
        cible["carac2"][4] = cible["carac2"][4] - Endurance_perdu
        print("La cible perd 50% de son endurance")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def Clairevoyance(lanceur,cible): #permet de voir toutes les statistiques des combattants
    if lanceur["carac2"][4] > 30:
        print("Quelles caractéristiques voulez vous voir?")
        print("1 : les vôtres (Coût de 30 d'endurance)")
        print("2 : celles de la cible (Coût de 30 d'endurance)")
        if lanceur["carac2"][4] > 60:
            print("3 : les deux (Coût de 60 d'endurance)")
        choixclairevoyance = int(input())
        if choixclairevoyance == 1:
            print("Clairevoyance lancé! Vos caractéristiques sont:")
            print(lanceur["carac2"])
            print("Dans l'ordre suivant : Vitesse, PV, Attaque, Defense, Endurance")
            lanceur["carac2"][4] = lanceur["carac2"][4] - 30
        elif choixclairevoyance == 2:
            print("Clairevoyance lancé! Ses caractéristiques sont:")
            print(cible["carac2"])
            print("Dans l'ordre suivant : Vitesse, PV, Attaque, Defense, Endurance")
            lanceur["carac2"][4] = lanceur["carac2"][4] - 30
        elif choixclairevoyance == 3:
            print("Clairevoyance lancé! Les caractéristiques sont:")
            print("Les vôtres (Vitesse, PV, Attaque, Defense, Endurance)")
            print(lanceur["carac2"])
            print("La cible (Vitesse, PV, Attaque, Defense, Endurance)")
            print(cible["carac2"])
            lanceur["carac2"][4] = lanceur["carac2"][4] - 60
        elif choixclairevoyance > 3:
            print("Vous n'avez pas choisis une option valable et par conséquent perdez votre tour (mdr)")
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def RemiseAzero(lanceur,cible):
    if lanceur["carac2"][4] > 70:
        print("Remise à zéro lancé! Coût de 70 d'endurance")
        PV_gardes = lanceur["carac2"][1]
        lanceur["carac2"] = lanceur["caracteristques"]
        print("Vos caractéristiques ont été rénitialisés!")
        lanceur["carac2"][1] = PV_gardes
    else:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")

def BoostAttaque(lanceur,cible):
    if lanceur["carac2"][4] < 30:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!")  
    else :
        print("Sort de Boost d'attaque lancé! Coût de 30 d'endurance")
        Attaque_gagne = 15 * lanceur["carac2"][1]/100
        Attaque_gagne=int(Attaque_gagne)
        cible["carac2"][2] = cible["carac2"][2] + Attaque_gagne
        cible["carac2"][4] = cible["carac2"][4] - 30
        print("Vous gagnez 30% de points d'attaques!")

def BoostDefense(lanceur,cible):
    if lanceur["carac2"][4] < 30:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!") 
    else:
        print("Sort de Boost de défense lancé! Coût de 30 d'endurance")
        Defense_gagne = 10 * lanceur["carac2"][3]/100
        Defense_gagne=int(Defense_gagne)
        cible["carac2"][3] = cible["carac2"][3] + Defense_gagne 
        cible["carac2"][4] = cible["carac2"][4] - 30
        print("Vous gagnez 10% de points de defense!")

def BoostDefenseSup(lanceur,cible):
    if lanceur["carac2"][4] < 60:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!") 
    else:
        print("Sort de Boost de défense supérieur lancé! Coût de 70 d'endurance")
        Defense_gagne = 30 * lanceur["carac3"][3]/100
        Defense_gagne=int(Defense_gagne)
        cible["carac2"][3] = cible["carac2"][3] + Defense_gagne
        cible["carac2"][4] = cible["carac2"][4] - 60
        print("Vous gagnez 30% de points de defense!")

def SortErrosion(lanceur,cible):
    if lanceur["carac2"][4] < 70:
        print("Le sort à échoué ... vous n'avez pas assez d'endurance!") 
    else:
        print("Sort d'Errosion lancé! Coût de 70 d'endurance")
        AllStats = lanceur["caracteristiques"][0,2,3,4] - lanceur["carac2"][0,2,3,4]/100
        cible["carac2"][0,2,3,4] = cible["carac2"][0,2,3,4] + AllStats 
        lanceur["carac2"][4] = lanceur["carac2"][4] - 70
        print("Votre cible voit ses caractéristiques rétitialisés!")

################### Sorts de monstres ###################

#Rick Bourré
def Picole(lanceur):
    if lanceur["carac2"][4] > 40:
        print("Rick Bourré lance Picole! Coût de 40 d'endurance")
        PV_gagne = 30 + (lanceur["carac2"][2]) * (lanceur["carac2"][3])/100
        PV_gagne=int(PV_gagne)
        lanceur["carac2"][1] = lanceur["carac2"][1] + PV_gagne
        if lanceur["carac2"][1] >= lanceur["caracteristiques"][1]:
            lanceur["carac2"][1] = lanceur["caracteristiques"][1]
        lanceur["carac2"][4] = lanceur["carac2"][4] - 40
        print("Rick Bourré récupère " +str(PV_gagne)+ " PV")
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")

def GueuleDeBois(lanceur):
    if lanceur["carac2"][4] > 30:
        print("Rick Bourré lance Gueule de bois! Coût de 30 d'endurance")
        gueuledeboisrandom = randint (1,2)
        if gueuledeboisrandom == 1:
            print("Oups! Il perd le contrôle et se blesse...")
            lanceur["carac2"][2] = lanceur["carac2"][2] - 30
            print("Rick Bourré perd 30 PV")
        else:
            print("Cela améliore sa défense physique! (l'abus d'alcool est dangereux pour la santé)")
            lanceur["carac2"][3] = lanceur["carac2"][3] + 10
            print("Rick Bourré gagne 10 points d'armure")
        lanceur["carac2"][4] = lanceur["carac2"][4] - 30
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")

def Molotov(lanceur,cible):
    if lanceur["carac2"][4] > 50:
        print("Rick Bourré lance une molotov! Coût de 50 d'endurance")
        molotovrandom = randint (1,5)
        if molotovrandom == 5:
            print("Il réussi son lancé!")
            PV_perdu = 40 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100
            PV_perdu=int(PV_perdu)
            cible["carac2"][1] = cible["carac2"][1] - PV_perdu
            print("Vous perdez " +str(PV_perdu)+ " PV")
            lanceur["carac2"][4] = lanceur["carac2"][4] - 50
        else:
            print("mais il rate son lancé...")
            print("Vous perdez 0 PV")
            lanceur["carac2"][4] = lanceur["carac2"][4] - 50
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")

#Morty Enragé
def PacteDeSang(lanceur,cible):
    if lanceur["carac2"][4] < 30:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")     
    else:
        print("Morty Enragé lance un Pacte de Sang! Coût de 30 d'endurance")
        Attaque_gagne = 25 * lanceur["carac2"][1]/100
        Attaque_gagne=int(Attaque_gagne)
        cible["carac2"][2] = cible["carac2"][2] + Attaque_gagne
        cible["carac2"][4] = cible["carac2"][4] - 30
        
        print("Il gagne un boost d'attaque de 25% mais son armure descend à 0")

def MorsureSauvage(lanceur,cible):
    if lanceur["carac2"][4] > 40:
        print("Morty Enragé lance Morsure Sauvage! Coût de 40 d'endurance")
        PV_perdu = 80 * (10 + (lanceur["carac2"][2]) * (cible["carac2"][3])/100)/100
        PV_perdu=int(PV_perdu)
        cible["carac2"][1] = cible["carac2"][1] - PV_perdu
        PV_gagne = PV_perdu - (20 * PV_perdu/100)
        PV_gagne=int(PV_gagne)
        lanceur["carac2"][1] = lanceur["carac2"][1] + PV_gagne
        if lanceur["carac2"][1] >= lanceur["caracteristiques"][1]:
            lanceur["carac2"][1] = lanceur["caracteristiques"][1]
        lanceur["carac2"][4] = lanceur["carac2"][4] - 40
        print("Vous perdez "+str(PV_perdu)+ " PV")
        print("Morty Enragé récupère " +str(PV_gagne)+ " PV")
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")

#Rick Rolled
def DesJetees(lanceur,cible):
    print("Rick Rolled lance le Dé Ultime! Coût de 30 d'endurance")
    DeeRandom = randint(1,6)
    if lanceur["carac2"][4] > 30:
        if DeeRandom == 1:
            lanceur["carac2"][2] = lanceur["carac2"][2] + 40
            print("Le Dé affiche 1 : Rick Rolled gagne 40 points de vie!")
        elif DeeRandom == 2:
            lanceur["carac2"][3] = lanceur["carac2"][2] + 20
            print("Le Dé affiche 2 : Rick Rolled gagne 20 points d'attaque!")
        elif DeeRandom == 3:
            lanceur["carac2"][3] = lanceur["carac2"][2] + 40
            print("Le Dé affiche 3 : Rick Rolled gagne 40 points de défense!")
        elif DeeRandom == 4:
            lanceur["carac2"][4] = lanceur["carac2"][2] + 50
            print("Le Dé affiche 4 : Rick Rolled gagne 50 points d'endurance!")
        elif DeeRandom == 5:
            cible["carac2"][2] = 1
            print("Le Dé affiche 5 : Vous descendez à 1 points d'attaque!")
        elif DeeRandom == 6:
            cible["carac2"][4] = 0
            print("Le Dé affiche 6 : Vous descendez à 0 points d'endurance!")
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")

def NeverGonnaGiveYouUp(lanceur,cible):
    if lanceur["carac2"][4] == 150:
        print("Rick Rolled lance Never Gonna Give You Up! Coût de 150 d'endurance")
        print("Ses caractéristiques sont renitialisés")
        lanceur["carac2"] = lanceur["caracteristques"]
    else:
        print("Mais il echoue ... Il n'a pas assez d'endurance!")