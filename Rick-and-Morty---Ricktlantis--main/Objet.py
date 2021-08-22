def StatObjet(obj):
    vit=0
    vit=0
    pv=0
    atk=0
    defense=0
    end=0
    condi=True
    where="armure"

    if obj == "Casque de garde":
        vit=1
        pv=1
        atk=1
        defense=1
        end=1
        condi=True
        where="armure"
        
    if obj == "Armure de garde":
        vit=2
        pv=2
        atk=2
        defense=2
        end=2
        condi=True
        where="armure"
    
    if obj == "Jambière de garde":
        vit=2
        pv=2
        atk=2
        defense=2
        end=2
        condi=True
        where="armure"


    if obj =="Bottes de garde":
        vit=2
        pv=2
        atk=2
        defense=2
        end=2
        condi=True
        where="armure"

    if obj=="Fusil Laser":
        vit=0
        pv=0
        atk=20
        defense=3
        end=3
        condi=True
        where="armes"

    
    return vit,pv,atk,defense,end,condi,where


