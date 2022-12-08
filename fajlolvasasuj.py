def kiolvas():
	olvas=[]
	#print("Fájl kiolvasás...\n")
	file=open("bookseries.txt", "r", encoding="utf-8")
	row=file.readline() #fejléc beolvasása
	
	munka = file.readlines() #sorok beolvasása
	for a in range(len(munka)):  #sorlista elemein végigmegy
		for i in range(0,5):  # sor szétválasztott elemein végigmegy
			row = munka[a]  #egy sor megfogása
			rowsp=row.split(":") #sor szétválasztása ":" mentén

			if len(row) > 1: # az utolsó, üres(csak egy whitespace) sor figyelmen kívül hagyása
				inst = rowsp[i].rstrip("\n") #utolsó listaelem végéről eltávolítja a whitespace-ket (\n itt)
				olvas.append(inst)
		print(olvas)
		olvas = []
	file.close()
	return olvas
kiolvas()
