import json   # json module is used to save and load data from a file

# This list stores all books in the library
# Each book is stored as a dictionary inside this list
library_books = []

# This function loads saved books from books.json file
# The function runs only once at the start of the program
def load_books():
    global library_books
    try:
        # Here, the file is opened to read its data
        with open("books.json", "r") as file:
            library_books = json.load(file)
    except:
        # If file does not exist, start with empty list
        library_books = []

# This function saves all book data into books.json file
# It runs when user exits the program
def save_books():
    with open("books.json", "w") as file:
        json.dump(library_books, file, indent=4)

# This function adds a new book from the user
# append() is used here to add data into the list
def add_book():
    book_name = input("Enter book name: ").strip()

    if book_name == "":
        print("Book name cannot be empty.")
        return

    library_books.append({
        "book_name": book_name,
        "book_status": "Available",
        "issue_date": "-"
    })

    print("Book added successfully.")

# This function displays all books in table format
def view_books():
    if not library_books:
        print("No books available.")
        return

    print("\n{:<5} {:<30} {:<15} {:<15}".format(
        "No.", "Book Name", "Status", "Issue Date"
    ))
    print("-" * 70)

    for i, book in enumerate(library_books, start=1):
        print("{:<5} {:<30} {:<15} {:<15}".format(
            i, book["book_name"], book["book_status"], book["issue_date"]
        ))

# This function is used to issue a book to the user
# The issue date is taken from the user in this function
def issue_book():
    view_books()

    if not library_books:
        return

    book_no = input("\nEnter book number to issue: ")

    if not book_no.isdigit():
        print("Please enter numbers only.")
        return

    book_no = int(book_no)

    if 1 <= book_no <= len(library_books):
        book = library_books[book_no - 1]

        if book["book_status"] == "Available":
            issue_date = input("Enter issue date (DD-MM-YYYY): ").strip()

            if issue_date == "":
                print("Issue date cannot be empty.")
                return

            book["book_status"] = "Issued"
            book["issue_date"] = issue_date
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Invalid book number.")

# This function removes a book
# pop() is used to delete the book from the list
# Issued books are not allowed to be deleted
def delete_book():
    view_books()

    if not library_books:
        return

    book_no = input("\nEnter book number to delete: ")

    if not book_no.isdigit():
        print("Please enter numbers only.")
        return

    book_no = int(book_no)

    if 1 <= book_no <= len(library_books):
        book = library_books[book_no - 1]

        if book["book_status"] == "Issued":
            print("Cannot delete this book. It is currently issued.")
            return

        removed_book = library_books.pop(book_no - 1)
        print("Book deleted successfully:", removed_book["book_name"])
    else:
        print("Invalid book number.")

# This function shows all available menu options
def show_menu():
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book (Enter Issue Date)")
    print("4. Delete Book")
    print("5. Exit")

# The program starts from this point
# Saved data is loaded before the program starts
load_books()

# Tis is main while loop
# This loop runs the program until the user exits
while True:
    show_menu()

    choice = input("Choose option: ")

    if not choice.isdigit():
        print("Please enter numbers only.")
        continue

    choice = int(choice)

    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        delete_book()
    elif choice == 5:
        save_books()
        print("Library closed. Data saved.")
        break
    else:
        print("Invalid option.")
