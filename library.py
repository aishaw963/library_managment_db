import sqlite3

while True:
    print("\n===== LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author: ")

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?)",
            (book_id, book_name, author)
        )

        conn.commit()
        conn.close()

        print("Book Added Successfully!")

    elif choice == "2":
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        if len(books) == 0:
            print("No books available.")
        else:
            print("\n===== BOOK LIST =====")
            for book in books:
                print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}")

        conn.close()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        