import adatok
def writeFile(List):

    header = "title:writer:age:category:language"
    file = open("bookseries.txt", "a", encoding='utf-8')
    file.write(header)
    file.write("\n")
    for i in List:
        count = 0
        for adatok in i:
            file.write(adatok)
            if count < 4:
                file.write(":")
                count +=1
        file.write("\n")
    file.close()
writeFile(adatok.imputList())