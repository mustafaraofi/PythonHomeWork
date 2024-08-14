#16. Create a class Library with attributes name and books (a list of Book objects). Provide methods to add and remove books.
class library:
    def __init__(self,name):
        self.name=name
        self.books=[]
            
    def add_book(self,book):
        self.books.append(book)
        print("the book added")
        
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print("the book removed")
        else:
            print("this book is not in the list")
    def get_book(self,name):
        if name in self.books:
            print(f"the {name} book is in library")
        else:
            print(f"the {name} book is not in library")

l=library(name="university library")
l.add_book("math")
        


        