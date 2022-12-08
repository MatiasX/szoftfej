def writeFile(List,fileName):
    
    for i in range(0, len(List)):
        file = open("{}.txt".format(fileName), "a", encoding='utf-8')
        file.write(List[i])
        if i < len(List)-1:
            file.write(":")
    file.write("\n")
    file.close()
    

from bookClass import Book
