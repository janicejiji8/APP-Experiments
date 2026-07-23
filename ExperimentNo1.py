class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"Patron: {self.name} | ID: {self.patron_id} | Books Borrowed: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added to catalog: '{book.title}'")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Registered new patron: {patron.name}")

    def borrow_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not patron:
            print(f"Error: Patron ID '{patron_id}' not found.")
            return
        if not book:
            print(f"Error: Book with ISBN '{isbn}' not found.")
            return

        if book.borrow():
            patron.borrow_book(book)
            print(f"Success: {patron.name} borrowed '{book.title}'.")
        else:
            print(f"Unavailable: '{book.title}' is already borrowed.")

    def return_book(self, patron_id, isbn):
        patron = next((p for p in self.patrons if p.patron_id == patron_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if patron and book and book in patron.borrowed_books:
            if book.return_book():
                patron.return_book(book)
                print(f"Success: {patron.name} returned '{book.title}'.")
        else:
            print(f"Error: Could not process the return for '{isbn}' by Patron ID '{patron_id}'.")

    def display_info(self):
        print("\n--- Current Library Catalog ---")
        for book in self.books:
            print(book)
        print("-------------------------------")


if __name__ == "__main__":
    mit_library = Library()

    print("\n--- Adding Books ---")
    book1 = Book("Clean Code", "Robert C. Martin", "9780132350884")
    book2 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
    book3 = Book("Design Patterns", "Erich Gamma", "9780201633610")
    
    mit_library.add_book(book1)
    mit_library.add_book(book2)
    mit_library.add_book(book3)

    print("\n--- Registering Patrons ---")
    patron1 = Patron("Alice Sharma", "P001")
    patron2 = Patron("Bob Patil", "P002")

    mit_library.register_patron(patron1)
    mit_library.register_patron(patron2)

    mit_library.display_info()

    print("\n--- Borrowing Books ---")
    mit_library.borrow_book("P001", "9781593279288") 
    mit_library.borrow_book("P002", "9781593279288") 
    mit_library.borrow_book("P002", "9780132350884") 

    mit_library.display_info()

    print("\n--- Returning Books ---")
    mit_library.return_book("P001", "9781593279288") 

    mit_library.display_info()
    
    print("\n--- Patron Status ---")
    print(patron1)
    print(patron2)
