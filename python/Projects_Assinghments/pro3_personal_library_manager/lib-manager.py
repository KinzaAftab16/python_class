import json
import os

data_file = 'library-manager.txt'

# function to load library 
def load_library ():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
        return []

# function to save library 
def save_library (library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

# function to add book in library 
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = input("Enter the book year: ")
    genre = input("Enter the book genre: ")
    read = input("Have you read the book? (yes/no): ").lower() == 'yes'

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(new_book)
    save_library(library)
    print(f'Book {title} added successfully.')

# function to remove book 
def remove_book(library):
    title = input("Enter the book title to remove the book: ")
    initial_lenght = len(library)
    library[:] = [book for book in library if book["title"].lower() != title]
    if len(library)< initial_lenght:
        save_library(library)
        print(f'Book {title} removed successfully.')
    else:
        print(f'Book {title} not found.')

# function to seacrch book
def seacrch_library(library):
    search_by = input("Enter the book tittle or author name.").lower()
    search_term = input(f"Enter the {search_by} ").lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print(f"No books found with '{search_term}' in the {search_by} feild.")

# function for display books 
def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
            print("No books in the library.")

def display_statistics(library):
    total_books= len(library)
    read_books = len([book for book in library if book["read"]])
    percentage_read= (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total Books: {total_books} ")
    print(f"Percentage Read : {percentage_read:.2f}%")
def main():
    library = load_library() 
    while True:
        print("Welcome To Personal Library Manager.")
        print("menu")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Display Status")
        print("6. Exit")

        choice = input("ENter your choice.")
        if choice == "1":
            add_book(library) 
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            seacrch_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            break
        else :
            print("Invalid choice.")
    
if __name__ == '__main__':
    main()
