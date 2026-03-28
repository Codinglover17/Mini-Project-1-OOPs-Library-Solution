# ============================================
# Project: Library Management System (OOP)
# Description: Simple OOP-based system to manage books and users
# ============================================

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    # Add Book
    def add_book(self, book):
        self.books[book.book_id] = book

    # Add User
    def add_user(self, user):
        self.users[user.user_id] = user

    # Issue Book
    def issue_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]

            if not book.is_issued:
                book.is_issued = True
                user.borrowed_books.append(book)
                print(f"Book '{book.title}' issued to {user.name}")
            else:
                print("Book already issued")
        else:
            print("Invalid book or user ID")

    # Return Book
    def return_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            user = self.users[user_id]

            if book in user.borrowed_books:
                book.is_issued = False
                user.borrowed_books.remove(book)
                print(f"Book '{book.title}' returned by {user.name}")
            else:
                print("This user did not borrow this book")

    # Display Books
    def display_books(self):
        for book in self.books.values():
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} by {book.author} - {status}")


# ===== Example Usage =====

library = Library()

# Add Books
library.add_book(Book(1, "Python Basics", "John"))
library.add_book(Book(2, "SQL Guide", "Mike"))

# Add Users
library.add_user(User(101, "Kamal"))
library.add_user(User(102, "Rahul"))

# Operations
library.issue_book(1, 101)
library.display_books()

library.return_book(1, 101)
library.display_books()
