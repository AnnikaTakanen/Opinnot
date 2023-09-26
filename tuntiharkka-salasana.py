def TarkistaSalasana(password):
    isStronk= True
    if len(password)< 8:
        isStronk=False
        print("salasana on alle 8 merkkiä")
    isotKirjaimet=0
    pienetKirjaimet=0   
    numerot=0
    erikoismerkki="!"#¤%&/(=?)
    for kirjain in password:
        if kirjain.isupper():
            isotKirjaimet+=1
        if kirjain.islower():
            pienetKirjaimet+=1
        if kirjain.isnumeric():
            numerot+=1
    for kirjain in password:
        for erikoismerkit
    if isotKirjaimet==0 or pienetKirjaimet==0:
        isStronk=False
        print("Salasanassa pitää  olla isoja ja pieniä kirjaimia")      
    if numerot==0:
        print("pitää olla myös numeroita")     
    return isStronk

onkoVahva= False
while onkoVahva==False:
    salasana=input("Anna salasana:")
    onkoVahva=TarkistaSalasana(salasana)
print("Hienoa!")          