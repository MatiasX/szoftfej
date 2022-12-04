import fajlolvasas 
import inputdata 
import konyv
import os.path
from pathlib import Path

def control():
	path = Path.cwd()  # megmondja az aktuális elérési útvonalát a fájlnak (az utolsó mappáig, a fájl neve nincs benne)
	path = str(path) + "\\bookseries.txt" #txt hozzáadása az elérési útvonalhoz 
	inputList = []
	outputList = []
	input0 = None
	#print(input0)
	header = "title:writer:release year:category:language\n"
	if os.path.isfile(path):  #ellenőrzi, hogy létezik e az adott file a megadott helyen
		file = open("bookseries.txt", "r", encoding="utf8")
		lenght = len(file.readlines()) 
		file.close()
	else:
		lenght = 1  #nincs ilyen file de hogy megnyissa a következő if, megadom hogy a hossza egy, így írásra nyílik meg a file
	if lenght > 1:  # ellenőrzi hogy van e a fejlécen kívül sor a file-ben
		file = open("bookseries.txt", "a", encoding='utf8')  #van, hozzáfűzésre nyitja meg
	elif lenght < 2:
		file = open("bookseries.txt", "w", encoding='utf8') #nincs, írásra nyitja meg, törli a tartalmát
		file.write(header) 

	file.close()
	while input0 != 0: 
		print("kilépéshez [0] kiolvasáshoz [1] bevitelhez [2] kereséshez [3]") #menü
		input0 = int(input("válassz:"))
		if input0 == 1:
			outputList.append(fajlolvasas.kiolvas()) #kiolvassa a sorokat, listába, listaelemeket szétválasztja, és kiírja a terminálba
		elif input0 == 2:
			inputList = inputdata.inputData() #bekér öt adatot az inputList-be
			konyv.writeFile(inputList,bookseries) #kiírja az inputListet egy sorba a file-ba ":"-val elválasztva
		else:
			break
	
control()
