def search(number):
	searchList = []
	file = open("bookseries.txt", "r", encoding="utf8")
	rows = file.readline()
	
	rows = file.readlines()
	print(len(rows))
	for i in range(len(rows)):
		row = rows[i]
		if len(row) > 0:
			
			rowSP = row.split(":")
							
			element = rowSP[number-1]
			x = element.rsplit()
							
	searchList.append(x)
	print(searchList)
	counter = 0
	for a in range(len(rows)-2 ):
		print("for",searchList)
		if str(x) == searchList[a]:
			continue
		elif a == counter -1 and str(x) != searchList[a]:
			searchList.append(x)
			counter += 1
	print(searchList)
	
	return
search(5)


