from book import Book

class KonyvInput():
 
    
    def konyvInput(book):
        # ~ book= "a" + str(nextline)
        # ~ book=Book()
        
        print("Adja meg a könyv adatait!\n")
        name=input("Könyv címe: ")
        book.title=name
        name=input("Írója: ")
        book.writer=name
        name=input("Kiadása: ")
        book.year=name
        name=input("Kategóriája: ")
        book.category=name
        name=input("Nyelve: ")
        book.language=name


