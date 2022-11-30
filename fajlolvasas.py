

def kiolvas(bookseries.txt):
	olvas=[]
	print("Fájl kiolvasás...\n")
	f=open("bookseries.txt", "r", encoding="utf-8")
	k=f.readline()
	while(k):
		k=f.readline()
		s=k.split(":")
		olvas.append(s)
		
	print(len(olvas))
	return olvas
