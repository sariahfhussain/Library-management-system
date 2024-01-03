# Library-management-system
This python program simulates a personal library management system. It allows users to manage a collection of books, including functionalities such as adding new books, displaying book details, and checking in/out books.
We firstly create a class, Books:
-In Python, a class is a blueprint or a template for creating objects. An object is an instance of a class, and classes are used to define the characteristics (attributes) and behaviors (methods) that the objects of the class will have.
A method is just a function that you define inside a class.

def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability
Then , the __init__ method initializes the attributes of a Book object (title, author, and availability) when a new book is created. This allows us to create instances of the Book class, each representing a specific book with its own title, author, and availability status.

def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")
        print("___________________")
We create a method to display the details.
the display_details method is called on a Book object, it prints out information about that book, including its title, author, and availability status. This method provides a user-friendly way to view the details of a book in the library management system.
print(f"Title: {self.title}"): Prints the title of the book using an f-string. It dynamically includes the title attribute of the current book object.
print(f"Author: {self.author}"): Prints the author of the book using an f-string. It dynamically includes the author attribute of the current book object.
print(f"Availability: {'Available' if self.availability else 'Not Available'}"): Prints the availability status of the book. It uses a ternary expression to determine whether the book is available or not and includes the result in the output.
print("___________________"): Prints a separator line to visually separate details of different books.


Now we create a method to check out books:
 def check_out(self):
        if self.availability:
            self.availability = False
            print(f"{self.title} has been checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

This method is responsible for simulating the process of checking out a book from the library, it turns the availability to not available when the book is checked out

Now we create a method to return a book:
 def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"{self.title} has been returned successfully.")
        else:
            print(f"{self.title} is already available.")








we create a Library class, to manage our collection of books and under this we
create methods to add books to the library and to display all books
class Library:
    def __init__(self):
        self.books = []


We create an __init__ method, which serves as the constructor. The purpose of the constructor is to initialize the object when it is created.This class has an __init__ method, which serves as the constructor. The purpose of the constructor is to initialize the object when it is created.

# creating a basic function to add books to our Library


    def add_book(self, book):
        self.books.append(book)


#func to display all books
    def display_all_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_details()

# now, we'll create a library named 'my_library', it is like a place that can hold books
my_library = Library()


# Now we are adding some books to book class,these are objects of book class, book1, book2 etc are variables
book1 = Book("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling")
book2 = Book("Norwegian Wood", "Haruki Murakami")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

# Now we are using the func add_book to add books to the library 'my_library'
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)


# now let's create a func so that the user can interact with our library


def user_interface(library):
    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Add new book")
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
                print(f"Book with title '{title}' not found in the library")


        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            for book in library.books:
                if book.title == title:
                    book.return_book()
                    break
            else:
                print(f"Book with title '{title}' not found in the library, you can add it to our lib by selecting option 2")


        elif choice == '5':
            print("BYE!")
            break


        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Run the user interface
user_interface(my_library)


Function Definition:
def user_interface(library): defines a function called user_interface that takes a library as its parameter. This function represents the interactive menu for the library management system.
Menu Display:
The while True: loop creates an infinite loop for the menu to keep prompting the user until they choose to exit (option 5).
The menu options are displayed using print statements.
User Input:
choice = input("Enter your choice (1-5): ") takes user input for the chosen menu option.
Menu Options:
The subsequent if-elif statements check the user's choice and execute the corresponding actions:
Option '1' displays all books using library.display_all_books().
Option '2' prompts the user to enter a new book's title and author, creates a new book object, and adds it to the library using library.add_book(new_book).
Option '3' prompts the user to enter the title of the book to borrow, and it calls the check_out method on the corresponding book in the library.
Option '4' prompts the user to enter the title of the book to return, and it calls the return_book method on the corresponding book in the library.
Option '5' prints a farewell message and breaks out of the loop, ending the program.
Invalid Input Handling:
The else statement handles cases where the user enters an invalid choice, prompting them to enter a number from 1 to 5.
Running the Interface:
The last line user_interface(my_library) runs the user interface, passing the my_library instance as an argument, allowing the user to interact with their personal library.
