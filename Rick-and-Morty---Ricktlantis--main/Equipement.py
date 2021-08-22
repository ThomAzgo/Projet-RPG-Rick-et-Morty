from Objet import *
from Joueur import *

def Equiper(joueur,obj):
    a=StatObjet(obj) #Recup les stats de l'item
    i=0 
    g=0
    while i<len(Player["equipement"]): #Cherche à quel est le type de l'item ex: casque,armure,....
        if a[6]==Player["equipement"][i][6] :
            break
        i=i+1
    
#######################################  
    if Player["equipement"][i][5]==False:  #On Commence par regarder si y'a déjà un équipement ou pas  ici c'est NON
        Player["equipement"][i]=list(a)
        while g<5:
            Player["caracteristiques"][g]=Player["caracteristiques"][g]+a[g]
            g=g+1     

    elif Player["equipement"][i][5]==True:  #On Commence par regarder si y'a déjà un équipement ou pas  ici c'est OUI
        Desequiper(Player,a[6])
        Player["equipement"][i]=list(a)
        while g<5:
            Player["caracteristiques"][g]=Player["caracteristiques"][g]+a[g]
            g=g+1
    




def Desequiper(joueur,endroit):
    i=0
    g=0
    while i<len(Player["equipement"]): #Cherche à quel est le type de l'item ex: casque,armure,....
        if endroit==Player["equipement"][i][6] :
            break
        i=i+1

    while g<5:         
        Player["caracteristiques"][g]=Player["caracteristiques"][g]-Player["equipement"][i][g]
        Player["equipement"][i][g]=0
        g=g+1
    Player["equipement"][i][g]=False
    
    



