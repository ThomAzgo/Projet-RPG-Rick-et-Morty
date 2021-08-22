from Joueur import *
from Game import *
from Sauvegarde import*
def MainMenu():
    print("Bienvenue sur notre jeu qui va être mega super cool promis")
    print("1 - Nouveau jeu")
    print("2 - Charger partie")
    print("3 - À  propos")
    print("4 - Quitter")
    choix=int(input())
    
    if choix==1:
        NewGame()
    if choix==2:
        l=Load(backpack)
        Game(l[0],l[1])
    if choix==3:
        About()
    if choix==4:
        Exit()
    else:
        print("Vous ne savez pas écrire")
        MainMenu()
     
def NewGame ():
    print("Vous commencez une nouvelle partie")
    #Initialisation de la partie
    Creation()
    #Fin initialisation
    print("Vous rentrez d'une mission et décidez de vous rendre au marché de RickLantis. Morty vous rejoint :")
    print("-Ouah ! Je suis KO ! Elle m'a tuée cette mission...")
    print("- Toujours à te plaindre einh ?! Allez Morty, on va se changer les idées. Allons boire un coup!")
    print("- Ouais...")
    print("Vous marchez sur le chemin du marché, rempli de Rick et de Morty différents.")
    print("-Eh Morty, regarde-moi ce p*tain de Fusil-Poulpe ! Je suis sûr que... ! ")
    print("Soudain, vous sentez le sol trembler sous vos pieds. Les objets en vente dans les stands  tremblent également.")
    print("-C'est Evil Morty ! Cachez-vous ! Cria un Rick vendeur.")
    print("Tous les Rick et Morty se mettent à crier et à s'affoler dans tous les sens.")
    print("Avant que nos deux personnages puissent comprendre , un lazer viens les propulser sur quelques mètres de distance...")
    print("et se font capturer.")
    print("C'est alors après quelques minutes que votre partenaire vous sauve en vous permettant de vous sauver.")
    print("Evil Morty s'enfuit et vous tentez de le rattraper.")
    attendre=input()
    Game(0,0) #On lance la partie



def About():
    print("Information")

def Exit():
    print("Vous quittez")


