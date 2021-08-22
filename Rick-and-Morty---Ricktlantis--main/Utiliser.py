from Joueur import*
def Utiliser (obj):

    if obj == "Potion de Soins" :
        print("Vous avez utilisé la Potion de Soins ! Elle vous rapporte 10 pv supplémentaires !")
        Player["carac2"][1] = Player["carac2"][1] + 10
        if Player["carac2"][1] > Player["caracteristiques"][1] :
            caracMax = Player["carac2"][1] - Player["caracteristiques"][1]
            Player["carac2"][1] = Player["carac2"][1] - caracMax
    

            















