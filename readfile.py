
class ReadFile:
	def readFile():
		read=[]
		file=open("bookseries.txt", "r", encoding="utf-8")
		header=file.readline() #fejléc beolvasása
		
		allLines = file.readlines() #sorok beolvasása
		for a in range(len(allLines)):  #sorlista elemein végigmegy
			for i in range(0,5):  # sor szétválasztott elemein végigmegy
				oneLine = allLines[a]  #egy sor megfogása
				oneLineSplit=oneLine.split(":") #sor szétválasztása ":" mentén

				if len(oneLine) > 1: # az utolsó, üres(csak egy whitespace) sor figyelmen kívül hagyása
					inst = oneLineSplit[i].rstrip("\n") #utolsó listaelem végéről eltávolítja a whitespace-ket (\n itt)
					read.append(inst)
			print("{}\t{}\t{}\t{}\t{}\t{}".format(read[0],read[1],read[2],read[3],read[4]))
			read = []
		file.close()


