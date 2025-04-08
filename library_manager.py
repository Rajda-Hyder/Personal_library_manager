#imports
import os 
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Automatically reset color after every print

#function for library.txt file
def load_lib():
    lib = []
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as file:
            for line in file:
                book_data = line.strip().split(' | ')
                if len (book_data) == 5:
                    book = {
                        "Title": book_data[0],
                        "Author": book_data[1],
                        "Year" : book_data[2],
                        "Genre" : book_data[3],
                        "Read" : book_data[4] == "Read"

                     }
                    lib.append(book)
    return lib

def save_lib(lib):
    with open("library.txt", "w") as file:
        for book in lib:
            status = "Read" if book["Read"] else "Unread"
            line = f'{book["Title"]} | {book["Author"]} | {book["Year"]} | {book["Genre"]} | {status}'
            file.write(line + "\n")

def add_book(lib):
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year: ")
    genre = input("Genre: ").strip().title()
    read = input("Have you read it? (yes/no): ").strip().lower() == "yes"
    read = read_input in ["yes", "y"]

    
    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }
    lib.append(book)
    save_lib(lib)
    print(Fore.GREEN + "✅ Book added!")

def remove_book(lib):
    title = input("Enter the title of the book to remove: ").strip()
    updated_lib = [book for book in lib if book["Title"].lower() != title.lower()]
    if len(updated_lib) != len(lib):
        save_lib(updated_lib)
        print(Fore.RED + "❌ Book removed.")
    else:
        print(Fore.YELLOW + "Book not found.")
    return updated_lib

def search_book(lib):
    keyword = input("Enter keyword to search: ").strip().lower()
    found = [book for book in lib if keyword in book["Title"].strip().lower()]
    if found:
        for book in found:
            print(f'- {book["Title"]} by {book["Author"]} ({book["Year"]}) [{book["Genre"]}] - {"Read" if book["Read"] else "Unread"}')
    else:
        print(Fore.RED + "No matching books found.")

def display_books(lib):
    if not lib:
        print("📭 No books in library.")
    else:
        for book in lib:
            print(f'- {book["Title"]} | {book["Author"]} | {book["Year"]} | {book["Genre"]} | {"Read" if book["Read"] else "Unread"}')

def display_stats(lib):
    total = len(lib)
    read = sum(book["Read"] for book in lib)
    percent = (read / total) * 100 if total > 0 else 0
    print(f"📚 Total Books: {total}")
    print(f"✅ Read: {read} ({percent:.1f}%)")
    print(f"📖 Unread: {total - read} ({100 - percent:.1f}%)")

def update_read_status(lib):
    title = input("Enter the title of the book to update status: ").strip().lower()
    found = False
    for book in lib:
        if book["Title"].lower() == title:
            book["Read"] = not book["Read"]  # Toggle True/False
            status = "Read" if book["Read"] else "Unread"
            print(Fore.CYAN + f"✅ Status updated to: {status}")
            found = True
            break

    if not found:
        print(Fore.RED + "❌ Book not found.")


# 📍 Main loop
library = load_lib()

while True:
    print(Back.MAGENTA + Fore.WHITE +"\t\t\t📚 WELCOME TO LIBRARY MANAGER 📚")
    print(Fore.GREEN + "1. 📕  Add a Book: ")
    print(Fore.BLUE + "2. ♻   Remove the Book: ")
    print(Fore.MAGENTA + "3. 🔎  Search for a Book: ")
    print(Fore.CYAN + "4. 📚  Display all Books: ")
    print(Fore.YELLOW + "5. 📊  Display Statistics(Total Books, Percentage Read): ")
    print(Fore.LIGHTMAGENTA_EX + "6. ✅  Mark Read/Unread Status")
    print(Fore.RED + "7. 🔚  Exit")
    

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_book(library)
    elif choice == "2":
        library = remove_book(library)
    elif choice == "3":
        search_book(library)
    elif choice == "4":
        display_books(library)
    elif choice == "5":
        display_stats(library)
    elif choice == "6":
        update_read_status(library)
    elif choice == "7":
        print(Fore.CYAN + "👋 Exiting Library Manager. Bye!")
        break
    else:
        print(Fore.RED + "❌ Invalid choice. Try again.")

