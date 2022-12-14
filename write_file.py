from book import Book
class WriteFile():

    def writeFile(book):
        # ~ book = "a" + str(nextLine)
        # ~ book = Book()
        file = open("bookseries.txt", "a", encoding="utf-8")
        file.write("\n")
        file.write(book.title)
        file.write(":")
        file.write(book.writer)
        file.write(":")
        file.write(book.year)
        file.write(":")
        file.write(book.category)
        file.write(":")
        file.write(book.language)
        
        file.close()
        



