class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.borrowed = {}

    def add_book(self):
        book = input("Enter book title: ")
        self.books.append(book)
        print(f"'{book}' added successfully!")

    def register_patron(self):
        patron = input("Enter patron name: ")
        self.patrons.append(patron)
        print(f"Patron '{patron}' registered successfully!")

    def borrow_book(self):
        book = input("Enter book to borrow: ")
        if book in self.books and book not in self.borrowed.values():
            patron = input("Enter patron name: ")
            if patron in self.patrons:
                self.borrowed[book] = patron
                print(f"'{book}' borrowed by {patron}.")
            else:
                print("Patron not registered.")
        else:
            print("Book unavailable or already borrowed.")

    def return_book(self):
        book = input("Enter book to return: ")
        if book in self.borrowed:
            del self.borrowed[book]
            print(f"'{book}' returned successfully!")
        else:
            print("This book wasn't marked as borrowed.")

    def display_books(self):
        print("\n--- Library Inventory ---")
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            status = "Borrowed" if book in self.borrowed else "Available"
            print(f"- {book} ({status})")
        print("-" * 25)


library = Library()

while True:
    print("\n========================================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_patron()
    elif choice == "3":
        library.borrow_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")