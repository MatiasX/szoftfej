#inputList = ["cym","adat", "2000", "balazs", "magyar"]
def writeFile(List):
    header = "title:writer:age:category:language"
    file = open("bookseries.txt", "w", encoding='utf-8')
    file.write(header)
    file.write("\n")
    for i in range(0, len(List)):
        file.write(List[i])
        file.write(":")
    file.close()
writeFile(inputList)

