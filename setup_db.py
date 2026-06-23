import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id TEXT,
    name TEXT,
    author TEXT
)
""")

# insert sample data
cursor.execute("INSERT INTO books VALUES (?, ?, ?)", ("101", "Python Basics", "John"))
cursor.execute("INSERT INTO books VALUES (?, ?, ?)", ("102", "C++ Guide", "Bjarne"))
cursor.execute("INSERT INTO books VALUES (?, ?, ?)", ("103", "Java Intro", "James"))

conn.commit()
conn.close()

print("Database created with sample data!")