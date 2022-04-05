# Library Management System -


class Library:
    def __init__(self, name, list):
        self.name = name
        self.list_of_books = list
        self.dictionary = {}

    def display_books(self):
        return(f"Available books in Library are: {self.list_of_books} \n")

    def add_book(self):
        book = input("Enter the book name: \n")
        if book in self.list_of_books:
            book_name = input(f"As {book} already in Library so naming must be like {book}2 \n")
            self.list_of_books.append(book_name)
        else:
            self.list_of_books.append(book)
        return("Your donated book has been added into the Library, Thank you ! \n")

    def borrow_book(self):
        book = input("Enter the book name: \n")
        user = input("Enter your name: \n")
        if book in self.list_of_books:
            if book not in self.dictionary.keys():
                self.dictionary.update({book:user})
                return("You borrow this book:",book)
            else:
                return("This book has been already borrowed by",self.dictionary.get(book))
        else:
            return("Sorry we do not have this book in Library !! \n")

    def return_book(self):
        book = input("Enter the book name: \n")
        if book in self.dictionary.keys():
            del self.dictionary[book]
            return("Thank you for returing a book:",book)
        else:
            return("You had not borrowed this book if you wish you can donate !! \n")
        


lib = Library("Nitin's Library",["Python","Java","C++","Django"])

print("Welcome into the Nitin's Library !!")
while(True):
    n = int(input("Type 1 for display_books, 2 for add_book, 3 for borrow_book, 4 for return_book \n"))
    if n == 1:
        print(lib.display_books())
    elif n == 2:
        print(lib.add_book())
    elif n == 3:
        print(lib.borrow_book())
    else:
        print(lib.return_book())








