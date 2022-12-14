class WriteFile(nextLine):
    book = "a" + nextline
    book = Book()
    def writeFile(book):
        file = open("bookseries.txt", "a" encoding="utf-8")
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


