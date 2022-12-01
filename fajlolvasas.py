

def kiolvas():
	olvas=[]
	#print("Fájl kiolvasás...\n")
	f=open("bookseries.txt", "r", encoding="utf-8")
	k=f.readline() #fejléc beolvasása
	
	x = f.readlines() #sorok beolvasása
	for a in range(len(x)):  #sorlista elemein végigmegy
		for i in range(0,5):  # sor szétválasztott elemein végigmegy
			k = x[a]  #egy sor megfogása
			s=k.split(":") #sor szétválasztása ":" mentén

			if len(k) > 1: # az utolsó, üres(csak egy whitespace) sor figyelmen kívül hagyása
				inst = s[i].rstrip("\n") #utolsó listaelem végéről eltávolítja a whitespace-ket (\n itt)
				olvas.append(inst)
		print(olvas)
		olvas = []
	f.close()
	return olvas
