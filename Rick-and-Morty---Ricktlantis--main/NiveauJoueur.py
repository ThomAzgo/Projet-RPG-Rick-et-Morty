from Joueur import*
def GainLVL ():
    LevelUp = Player["lvl"][0] * 10 #La variable LevelUp est le nombre d'xp requis pour passer au niveau suivant
    if LevelUp <= Player["lvl"][1]:
        reste = Player["lvl"][1] - LevelUp
        Player["lvl"][0] = Player["lvl"][0] + 1
        Player["lvl"][1] = reste
        LevelUp = Player["lvl"][0] * 10
      #######################################  
        if Player["lvl"][0]==2:
                Player["Sort"].append("Armor Breaker 3003 : Réduit l'armure coûte 50 endurance") #SORT COROSIF ARMURE
                Player["Sort"].append("Turbo Flemme : Réduit l'endurance de l'ennemi coûte 30 d'enrucance")
                Player["Sort"].append("Dopage douteux: Boost d'attaque coûte 30 d'enrucance")
                Player["Sort"].append("Rick-cola : Boost de def coûte 30 d'enrucance")
        if Player["lvl"][0]==3:
            Player["Sort"].append("Méga-Sangsue : Drain de vie sur la cible coûte 40 d'endurance")
            Player["Sort"].append("Google Glass v69420 : Permet de voir les stats de la cible coûte 30 d'endurance pour une cible unique et 60 pour voir les tiennes plus celles du monstre")
            Player["Sort"].append("Doliprane mk2 : Soins supérieur coûte 40 d'endurance")
            Player["Sort"].append("X Æ A-12 : Reset tes stats à 0")
        if Player["lvl"][0]==4:
            Player["Sort"].append("Rick-cola Zero : Boost de def supérieur coûte 60 d'endurance")
            Player["Sort"].append("Nanorobots 5G : Boost d'endurance possible si on est en dessous de 30 d'endurance")
            Player["Sort"].append("Reformatage USB : Reset toutes les stats de l'ennemi sauf les pv")


    Player["Sort"]=list(set(Player["Sort"]))
    

def GainXP (xp):
    Player["lvl"][1] = Player["lvl"][1]  + xp
    GainLVL()


