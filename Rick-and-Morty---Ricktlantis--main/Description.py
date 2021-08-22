 
descriptionMap = {

    "0,0" : ["Vous êtes au centre de la carte. Vous voyez un panneau ; vers le Nord vous trouverez le quartiers des Affaires, vers le Sud le Hangar Spatial, vers l'Est l'Arène et vers l'Ouest vous trouverez le Bidonville.","Erreur",False],
    "1,0" : ["Vous êtes sur une passerelle. Vous voyez un panneau; avec écrit en continuant sur la droite vous irez vers l'arène, à gauche vous reviendrez sur vos pas, en haut vers le quartier Nord-Est et au sud le quartier Sud-Est","Erreur",False],
    "2,0": ["Vous avez pris l'ascenceur à votre droite ce trouve la sortie, à gauche vous pouvez remonter","Erreur",False],
    "3,0": ["Vous voilà face à un adversaire il porte le numéro 1 sur son dos, vous pouvez fuir en revenant sur vos pas","Il n'y plus rien ici",False],
    "-1,1" : ["Vous êtes sur une passerelle. Un Morty Super Sayan et vous tends un casque que voulez vous faire ?","Il n'y a plus personne",False],
    "-2,0": ["Vous avez pris l'ascenceur à votre gauche ce trouve la sortie, à droite vous pouvez remonter","Erreur",False],
    "-3,0": ["Vous voici face à un enemie il porte le numéro 3, vous pouvez fuir en revenant sur vos pas","Il n'y a rien ici pour le moment",False],
    "0,1" : ["Vous êtes sur une passerelle. Vous voyez un panneau avec écrit ; En continuant vers le haut vous irez vers le quartier des affaires, en bas vous reviendrez sur vos pas, à droite vers le quartier Nord-Est et à gauche le quartier Nord-Ouest","Erreur",False],
    "0,2" : ["Vous êtes devant un point de passage et les gardes sont affolés. ","Il n'y a plus de Garde. Tout le monde est partie",False],
    "0,3" : ["Vous avez pris l'ascenceur en bas ce trouve la sortie, en haut vous accedez au quartier des affaires","Erreur",False],
    "0,4" : ["Vous voici face à un enemie il porte le numéro 2 , vous pouvez fuir en revenant sur vos pas","Il n'y a rien ici pour le moment.",False],
    "0,-1": ["Vous êtes sur une passerelle. Vous voyez un panneau avec écrit ; En continuant vers le bas vous irez vers le hangar spatial, en haut vous reviendrez sur vos pas, à droite vers le quartier Sud-Est et à gauche le quartier Sud-Ouest","Erreur",False],
    "0,-2": ["Vous voici dans le hangar Spatial, vous ne pouvez acceder à aucun vaisseau car vous n'avez pas les clées","Vous voici dans le hangar Spatial, vous avez les clées, vous pouvez acceder au vaisseau",False],
    "1,1":["Vous êtes dans un hangar. Il y'a au sol un Plastron de garde. Que faire ?","Il n'y a rien à voir ici.",False],
    "-1,-1":["Vous êtes dans une ruelle sombre de la vielle dans laquelle vous venez d'entrer et vous appercevez dans une poubelle des jambières de garde.","Il n'y a plus rien ici",False],
    "-1,0":["Vous êtes sur une passerelle","Erreur",False],
    "1,-1":["Un garde vous propose ses chaussures contre la mise à mort d'Evil Morty.","Il n'y a plus rien ici.",False]

}



def Description(x,y,descriptionMap):
    if str(x)+","+str(y) in descriptionMap:
        if descriptionMap[str(x)+","+str(y)][2]==False:
            print(descriptionMap[str(x)+","+str(y)][0])
        elif descriptionMap[str(x)+","+str(y)][2]==True:
            print(descriptionMap[str(x)+","+str(y)][1])
        
