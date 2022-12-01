def writeFile(List):
    
    for i in range(0, len(List)):
        file = open("bookseries.txt", "a", encoding='utf-8')
        file.write(List[i])
        if i < len(List)-1:
            file.write(":")
    file.write("\n")
    file.close()
    

