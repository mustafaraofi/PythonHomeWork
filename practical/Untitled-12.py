#12. Create a class Book with private attributes title, author, and pages. Provide public methods to get and set these attributes
class book:
    def __init__(self,title,author,pages):
        self.__title=title
        self.__author=author
        self.__pages=pages
        
    def bookinfo(self):
        print(self.__title)
        print(self.__author)
        print(self.__pages)
        
book=book(title="math",author="thomas",pages=1200)
book.bookinfo()