from Description import *
from Interaction import * 
def Mouvement(Xx,Yy):
    print("Où veux-tu aller?")
    print("1 = Haut")
    print("2 = Gauche")   
    print("3 = Droite")
    print("4 = Bas")
    x = Xx
    y = Yy
    m = input()
    
    if m == "1":
        if str(x)+","+str(y+1) in descriptionMap:
            y = y + 1
        else :
            print("Vous ne pouvez pas aller par la")

    elif m == "2":
        if str(x-1)+","+str(y) in descriptionMap:
            x = x - 1
        else :
            print("Vous ne pouvez pas aller par la")

    elif m == "3":
        if str(x+1)+","+str(y) in descriptionMap:
            x = x + 1
        else :
            print("Vous ne pouvez pas aller par la")

    elif m == "4":
        if str(x)+","+str(y-1) in descriptionMap:
            y = y - 1
        else :
            print("Vous ne pouvez pas aller par la")
   
    else:
        print ("Erreur : tu n'as pas choisis une option valable")

    return x,y
