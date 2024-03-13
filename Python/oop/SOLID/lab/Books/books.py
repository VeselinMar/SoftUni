class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        if book not in self.books:
            self.books.append(book)
            return f"{book} added to {self.name}."
        else:
            return f"{book} is already in {self.name}."

    def find_book(self, book: Book):
        if not self.books:
            return f"{book} is not available in {self.name}."

        for book_in_library in self.books:
            if book_in_library == book:
                return f"{book} is available in {self.name}."
            else:
                return f"{book} is not available in {self.name}."

    def remove_book(self, book: str):
        for book_in_library in self.books:
            if book_in_library.title == book:
                self.books.remove(book_in_library)
                return f"{book} has been removed form {self.name}."
            else:
                return f"{book} is missing from {self.name}."


book1 = Book("StoyanPodMosta", "Stoyan")
library = Library("Vienna City Library")
print(library.add_book(book1))
print(library.find_book(book1))
print(library.remove_book("StoyanPodMosta"))
print(library.find_book(book1))