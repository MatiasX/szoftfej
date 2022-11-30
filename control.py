import


def control():
	inputList = []
	print("kilépéshez [0] kiolvasáshoz [1] bevitelhez [2]")
	input0 = input("válassz:")
	header = "title:writer:age:category:language"
    file = open("bookseries.txt", "w", encoding='utf-8')
    file.write(header)
    file.write("\n")
	while input0 != 0:
		if input0 == 1:
			olvas()
		elif input0 = 2:
			inputData(inputList)
			writeFile(inputList)
		else:
			break
	
	
