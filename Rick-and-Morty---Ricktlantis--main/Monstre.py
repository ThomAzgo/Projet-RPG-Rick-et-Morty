from random import*

def PickAMonster(): #carac=[vitesse,pv,atk,def,end]
      
    a=choice(Liste)
    return a



RickBourré = {
    "classe":"Rick Bourré",
    "caracteristiques":[5,115,10,10,150], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[5,115,10,10,100],
    "Sort":["Picole","GueuleDeBois","MolotovBourre"]
}      

MortyEnragé = {
    "classe":"Morty Enragé",
    "caracteristiques":[25,50,20,5,150], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[25,50,20,5,100],
    "Sort":["PacteDeSang","MorsureSauvage"]
}

LarbinRemonté = {
    "classe":"Larbin Corrompu",
    "caracteristiques":[15,100,15,15,150], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[15,100,15,15,100],
    "Sort":["Soins","BoostEndurance","BoostAttaque"]
}

Liste=[MortyEnragé,LarbinRemonté]

Boss = {
    "classe":"Rick Rolled",
    "caracteristiques":[15,200,5,40,150], #Vitesse, PV, Attaque, Defense, Endurance 
    "carac2":[15,200,5,30,150],
    "Sort":["DesJetees","NeverGonnaGiveYouUp"]
}