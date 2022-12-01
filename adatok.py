import random
def imputList():
    szerzo = ["Balázs Máté","Juhász Marci","Bognár Károly","Karikó Ferenc","Kosza József","Csituny János","vasas Milán","violin Panna","Hisztis Mirtil","Kukac Péter"]
    nyelv = ["Magyar","Angol","Német","Szerb","Ukrán","Japán","Kínai","Olasz","Francia","Cseh"]
    mufaj = ["Dráma","Erotika","Krimi","Akció","Művész","Életrajz","Kaland","Vígjáték","Történelmi","Sci-fi"]
    datum = ["2007","2022","2003","2002","2008","2015","2016","2017","2019","2012"]
    cim = ["rózsadomb","aranykutya","sejtek","4 kutyaélet","domb","orrfújás","katyvasz","tavasz","életmentő","kudarc"]
    listresult = []
    db = 0
    while db!=100:
        ok = True
        db += 1
        while ok:
            listtemp = []
            listtemp.append(szerzo[random.randint(0,9)])
            listtemp.append(nyelv[random.randint(0,9)])
            listtemp.append(mufaj[random.randint(0,9)])
            listtemp.append(datum[random.randint(0,9)])
            listtemp.append(cim[random.randint(0,9)])
            listresult.append(listtemp)
            ok = False
    return listresult
imputList()