# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
# Book class and adds the book to books list for current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
# the specified author
# - group_by_year(year: int) - returns a list of all books grouped by the
# specified year

# All 3 classes must have a readable __repr__ method!

# Also, book class should have a class variable which holds the amount of
# all existing books

# Task 2 extends the first one. Now you should add 2-3 types of books (for
# example, Schoolbook, Magazine etc)

# Library class should still have only one list for all books in contains
# but different methods for grouping by types. For example:
#   - fetch_schoolbooks
#   - fetch_magazines


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = set()

    def __repr__(self):
        return self.name

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.add(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
       return [book for book in self.books if book.year == year]

    def fetch_schoolbooks(self):
        return [book for book in self.books if isinstance(book, SchoolBook)]

    def fetch_magazines(self):
        return [book for book in self.books if isinstance(book, Magazine)]


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    def __repr__(self):
        return f"{self.name}"


class Book:

    amount = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.amount +=1
        self.author.books.append(self)

    def __repr__(self):
        return f"'{self.name}' by {self.author.name}"


class SchoolBook(Book):
    pass


class Magazine(Book):
    pass
