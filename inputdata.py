import re
informations=[]

def inputdata(informations):
    print("Szükséges adatok: könyv címe, író, kiadás éve, kategória, nyelv")
    for i in range(0,5):
        answer=(input("Kérem az adatokat:"))
        informations.append(answer)
    #print(informations)
    return informations
inputdata(informations)
