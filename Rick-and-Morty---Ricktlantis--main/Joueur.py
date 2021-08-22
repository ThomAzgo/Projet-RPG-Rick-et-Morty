Player = {
    "lvl" : [1,0],
    "equipement" : [[0,0,0,0,0,False,"casque"],[0,0,0,0,0,False,"armure"],[0,0,0,0,0,False,"pantalon"],[0,0,0,0,0,False,"bottes"],[0,0,0,0,0,False,"armes"]], #Casque,Armure,Pantalon,Bottes,Arme
}

def Creation() :
    
    print("Choisissez votre personnage :")
    print("1 = Rick")
    print("2 = Morty")
    joueur = int(input())
    
    if joueur == 1 :
        Player["classe"]="Rick"
        Player["caracteristiques"]=[10,115,15,15,100] # Vitesse/PV/ATTAQUE/DEF/ENDURANCE
        Player["carac2"]=[10,115,15,15,100]
        Player["Sort"]=["Doliprane mk1","Armor Breaker 3003  Réduit l'armure coûte 50 endurance","Turbo Flemme  Réduit l'endurance de l'ennemi coûte 30 d'enrucance","Dopage douteux Boost d'attaque coûte 30 d'enrucance","Rick-cola  Boost de def coûte 30 d'enrucance","Méga-Sangsue  Drain de vie sur la cible coûte 40 d'endurance","Google Glass v69420  Permet de voir les stats de la cible coûte 30 d'endurance pour une cible unique et 60 pour voir les tiennes plus celles du monstre","Doliprane mk2  Soins supérieur coûte 40 d'endurance","X Æ A-12  Reset tes stats à 0","Rick-cola Zero  Boost de def supérieur coûte 60 d'endurance","Nanorobots 5G  Boost d'endurance possible si on est en dessous de 30 d'endurance","Reformatage USB  Reset toutes les stats de l'ennemi sauf les pv"]
        
    elif joueur == 2 :
        Player["classe"]="Morty"
        Player["caracteristiques"]=[20,75,15,10,150]
        Player["carac2"]=[20,75,15,10,150]
        Player["Sort"]=["Doliprane mk1","Armor Breaker 3003  Réduit l'armure coûte 50 endurance","Turbo Flemme  Réduit l'endurance de l'ennemi coûte 30 d'enrucance","Dopage douteux Boost d'attaque coûte 30 d'enrucance","Rick-cola  Boost de def coûte 30 d'enrucance","Méga-Sangsue  Drain de vie sur la cible coûte 40 d'endurance","Google Glass v69420  Permet de voir les stats de la cible coûte 30 d'endurance pour une cible unique et 60 pour voir les tiennes plus celles du monstre","Doliprane mk2  Soins supérieur coûte 40 d'endurance","X Æ A-12  Reset tes stats à 0","Rick-cola Zero  Boost de def supérieur coûte 60 d'endurance","Nanorobots 5G  Boost d'endurance possible si on est en dessous de 30 d'endurance","Reformatage USB  Reset toutes les stats de l'ennemi sauf les pv"]
        
    
    else :
        print("Veuillez séléctionner 1 ou 2")
        Creation()

    print("Bonjour "+Player["classe"]+" !")

def VoirStat():
    print("Voici vos stats : ")
    print("Vitesse : "+str(Player["caracteristiques"][0])+", vos PV MAX : "+str(Player["caracteristiques"][1])+", votre attaque : "+str(Player["caracteristiques"][2])+", votre def : "+str(Player["caracteristiques"][3])+" et votre endurance : "+str(Player["caracteristiques"][4]))
    print(" ")
    print("Voici vos pv restants : "+str(Player["carac2"][1]))
        
    






















