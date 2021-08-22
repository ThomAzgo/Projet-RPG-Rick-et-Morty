from Description import *
from Interaction import *
from Game import*
from Inventaire import*
from Combat import*


dicoQuetePasActive={
    #Texte+QueteLancé+Statut+Condition+Récompenses+QueteSuivante
    "2" : ["Vous avez tabassé le premier boss au suivant 1/3","Combat","0","4"],
    "3" : ["Vous avez tabassé le deuxième boss au suivant 2/3","Combat","-3","0"],
    "4" : ["Vous avez tabassé le dernier boss et récuperé les clefs ! Retourne au vaisseau !","Fin","0","-2"],
    "5" :["Fin","oue","999","999"]
}

dicoQueteActive={
   "1": ["Votre partenaire à été kidnapé. Affrontez les 3 boss pour recup les clées du vaisseau","Combat","3","0","BossTest"],
   "g": "Votre partenaire à été kidnapé. Affrontez les 3 boss pour recup les clées du vaisseau"
}


dicoObj={
    "0,2":[False,"Fusil Laser","equipement"],
    "-1,1":[False,"Casque de garde","equipement"],
    "1,1":[False,"Armure de garde","equipement"],
    "-1,-1":[False,"Jambière de garde","equipement"],
    "1,-1":[False,"Bottes de garde","equipement"]
}

def QuêteSuivante(x,y,nQuete):
    
    descriptionMap[str(x)+","+str(y)][2]=True  
    del dicoQueteActive[nQuete]
    nQuete=int(nQuete)+1
    nQuete=str(nQuete)
    dicoQueteActive[nQuete]=dicoQuetePasActive[nQuete]
    dicoQueteActive["g"]=dicoQueteActive[nQuete]
    
    return nQuete
    
    
    
    
def VerfifCondition(x,y,nQuete,backpack,interaction):
    a="rien"
    b="rien"
    
    if str(x)==dicoQueteActive[nQuete][2] and str(y)==dicoQueteActive[nQuete][3]:
        if dicoQueteActive[nQuete][1]=="Combat":
            print("VOUS LANCEZ UN COMBAT")
            print(interaction[str(x)+","+str(y)][2])
            c=Combat(OrdreDePassage(Boss))
            if c=="perdu":
                quit()
            else:
                Recompenses(str(x),str(y))
                a=QuêteSuivante(x,y,nQuete)
            
        
        
        elif dicoQueteActive[nQuete][1]=="Action":
            print("VOUS LANCEZ UNE ACTION")
            a=QuêteSuivante(x,y,nQuete)
            

        elif dicoQueteActive[nQuete][1]=="Fin":
            print("C'est la fin de la partie 1")
            a=QuêteSuivante(x,y,nQuete)
                
        b=True
   
            

    elif str(x)+","+str(y) in dicoObj:
        if(dicoObj[str(x)+","+str(y)][0]==False):
            descriptionMap[str(x)+","+str(y)][2]=True
            AjouterInventaire(backpack,dicoObj[str(x)+","+str(y)][1],dicoObj[str(x)+","+str(y)][2])
            print(interaction[str(x)+","+str(y)][2])
            attendre=input()
            a=None
            b=False
            return a,b
        
    return a,b 
            
    
        





