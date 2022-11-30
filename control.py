import


def control():
	inputList = []
	print("kilépéshez [0] kiolvasáshoz [1] bevitelhez [2]")
	input0 = input("válassz:")
	
	while input0 != 0:
		if input0 == 1:
			olvas()
		elif input0 = 2:
			inputData(inputList)
			writeFile(inputList)
		else:
			break
	
	
