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

def main():
    while True:
        print("===== Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

main()
