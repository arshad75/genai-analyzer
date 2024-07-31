# Print out the details of a book
def print_book_details(book):
    """
    Prints out the details of the book.

    Args:
        book: The book to print the details of.
    """

    print("Title:", book.title)
    print("Author:", book.author)
    print("Genre:", book.genre)
    print("Price:", book.price)

# Print out the details of multiple books
def print_books_details(*books):
    """
    Prints out the details of multiple books.

    Args:
        *books: The books to print the details of.
    """

    for book in books:
        print_book_details(book)