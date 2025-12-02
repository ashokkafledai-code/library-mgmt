# Simple Library Management System

library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    library.append({"title": title, "author": author, "available": True})
    print("Book added!\n")

def view_books():
    if not library:
        print("No books in the library.\n")
        return

    for i, book in enumerate(library):
        status = "Available" if book["available"] else "Not Available"
        print(f"{i + 1}. {book['title']} by {book['author']} - {status}")
    print()

def borrow_book():
    view_books()
    num = int(input("Choose book number to borrow: ")) - 1

    if 0 <= num < len(library) and library[num]["available"]:
        library[num]["available"] = False
        print("Book borrowed!\n")
    else:
        print("Book not available.\n")

def return_book():
    view_books()
    num = int(input("Choose book number to return: ")) - 1

    if 0 <= num < len(library) and not library[num]["available"]:
        library[num]["available"] = True
        print("Book returned!\n")
    else:
        print("Book is already available.\n")

