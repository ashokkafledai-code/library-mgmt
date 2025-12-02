from books import add_book, view_books, borrow_books, return_books

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
          
if __name__ == "__main__":
  main()
