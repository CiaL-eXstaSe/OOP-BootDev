"""
=================
Wizard Library
=================

Description
-----------
A management system for wizard libraries to track their book collections.
Manual tracking is required as magical book-finding spells haven't been invented yet.

Challenge Details
----------------
Implement a library system with Book and Library classes for managing magical texts.

Class Structure
==============

Book Class
---------
Constructor Parameters:
- title: Book's title
- author: Book's author

Library Class
------------
Constructor Parameters:
- name: Library's name
- books: List to store Book instances (initialized empty)

Methods:
- add_book(book): Appends Book instance to books list
- remove_book(book): Removes book if title and author match
- search_books(search_string): Returns list of books matching search string
  (case-insensitive search in title or author)
"""
class Book:
    def __init__(self, title, author):
        # Initialize a new Book object with title and author attributes
        # These attributes store the basic information needed to identify a book
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        # Initialize a new Library with a name and an empty list to store books
        # The books list will contain Book objects that belong to this library
        self.name = name
        self.books = []

    def add_book(self, book):
        # Add a new book to the library's collection
        # Simply appends the book object to the books list
        self.books.append(book)

    def remove_book(self, book):
        # Remove a book from the library if both title and author match
        # Uses a slice copy of the list to safely modify during iteration
        for lib_book in self.books[:]:  # Create copy to avoid modification during iteration
            if lib_book.title == book.title and lib_book.author == book.author:
                self.books.remove(lib_book)

    def search_books(self, search_string):
        # Search for books where the search string appears in either title or author
        # Parameters:
        #   search_string: The text to search for in book titles and authors
        # Returns:
        #   A list of Book objects that match the search criteria
        
        # Convert search string to lowercase for case-insensitive comparison
        search_string = search_string.lower()
        
        # Use list comprehension to find all books where the search string
        # appears in either the title or author (case-insensitive)
        return [book for book in self.books 
                if search_string in book.title.lower() 
                or search_string in book.author.lower()]

# Solution below:
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
    
#     def add_book(self, book):
#         self.books.append(book)
    
#     def remove_book(self, book):
#         for lib_book in self.books[:]:  # Create copy to avoid modification during iteration
#             if lib_book.title == book.title and lib_book.author == book.author:
#                 self.books.remove(lib_book)
    
#     def search_books(self, search_string):
#         search_string = search_string.lower()
#         return [book for book in self.books 
#                 if search_string in book.title.lower() 
#                 or search_string in book.author.lower()]

