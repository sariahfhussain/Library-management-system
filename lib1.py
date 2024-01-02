# creating a Python program that simulates a personal library management system

# First we go ahead and create a Book class with attributes book title, author, and availability status
class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def display_details(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")
        print("___________________")

    def check_out(self):
        if self.availability:
            self.availability = False
            print(f"{self.title} has been checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"{self.title} has been returned successfully.")
        else:
            print(f"{self.title} is already available.")


'''here we create a Library class, to manage our collection of books and under this we 
create methods to add books to the library and to display all books  '''

class Library:
    def __init__(self):
        self.books = []

# creating a basic function to add books to our Library
    def add_book(self, book):
        self.books.append(book)

    def display_all_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_details()

# now, we'll create a library named 'my_library', it is like a place that can hold books
my_library = Library()

# Now we are adding some books to our library, book1, book2 etc are variables 
book1 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling")
book2 = Book("Norwegian Wood", "Haruki Murakami")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Jungle Book", "Rudyard Kipling")
book5 = Book("Charlie and the Chocolate Factory", "Roald Dahl")
book6 = Book("Atomic Habits", "James Clear")

# Now we are using the func add_book to add bokks to the library 'my_library'
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)

# Now we are adding some books to our library
book1 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling")
book2 = Book("Norwegian Wood", "Haruki Murakami")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Jungle Book", "Rudyard Kipling")
book5 = Book("Charlie and the Chocolate Factory", "Roald Dahl")
book6 = Book("Atomic Habits", "James Clear")

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)
my_library.add_book(book6)

# now let's create a func so that the user can interact with our library
def user_interface(library):
    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Add a book to our Library")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_all_books()

        elif choice == '2':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            new_book = Book(title, author)
            library.add_book(new_book)
            print("Book added successfully!")

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            for book in library.books:
                if book.title == title:
                    book.check_out()
                    break
            else:
                print(f"Book with title '{title}' not found in the library.")

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            for book in library.books:
                if book.title == title:
                    book.return_book()
                    break
            else:
                print(f"The Book:'{title}' is not a part of our library, you can add this book by selecting option 1 instead")

        elif choice == '5':
            print("BYE!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the user interface
user_interface(my_library)