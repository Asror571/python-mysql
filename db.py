def create_books_table(cursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(64) NOT NULL,
            author VARCHAR(64) NOT NULL,
            published_year INT NOT NULL,
            genre VARCHAR(64),
            price INT NOT NULL,
            available BOOLEAN DEFAULT TRUE
        );
    """)
    print("'Books' jadvali yaratildi yoki allaqachon mavjud.")


def insert_book(cursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """
    query = """
        INSERT INTO Books (title, author, published_year, genre, price, available)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (title, author, published_year, genre, price, available))
    print(f"Kitob qo'shildi: {title}")


def show_all_books(cursor):
    """
    Retrieve and display all books from the 'books' table.
    """
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    if books:
        print("\nKutubxonadagi kitoblar:")
        for book in books:
            print(f"ID: {book[0]}, Nomi: {book[1]}, Muallif: {book[2]}, Yil: {book[3]}, "
                  f"Janr: {book[4]}, Narx: {book[5]}, Mavjud: {'Ha' if book[6] else 'Yo‘q'}")
    else:
        print("Kutubxonada kitoblar yo'q.")


def search_books_by_author_or_genre(cursor, search_type, search_value):
    """
    Search for books by author or genre.
    """
    query = f"SELECT * FROM Books WHERE {search_type} = %s"
    cursor.execute(query, (search_value,))
    books = cursor.fetchall()
    if books:
        print(f"\n{search_type.capitalize()} bo'yicha topilgan kitoblar:")
        for book in books:
            print(f"ID: {book[0]}, Nomi: {book[1]}, Muallif: {book[2]}, Yil: {book[3]}, "
                  f"Janr: {book[4]}, Narx: {book[5]}, Mavjud: {'Ha' if book[6] else 'Yo‘q'}")
    else:
        print(f"{search_value} bo'yicha kitob topilmadi.")


def update_book_price(cursor, book_id, new_price):
    """
    Update the price of a specific book.
    """
    query = "UPDATE Books SET price = %s WHERE id = %s"
    cursor.execute(query, (new_price, book_id))
    if cursor.rowcount > 0:
        print(f"Kitob narxi yangilandi. ID: {book_id}, Yangi narx: {new_price}")
    else:
        print(f"ID: {book_id} bo'lgan kitob topilmadi.")


def update_book_availability(cursor, book_id, available):
    """
    Update the availability of a specific book.
    """
    query = "UPDATE Books SET available = %s WHERE id = %s"
    cursor.execute(query, (available, book_id))
    if cursor.rowcount > 0:
        print(f"Kitob mavjudligi yangilandi. ID: {book_id}, Mavjud: {'Ha' if available else 'Yo‘q'}")
    else:
        print(f"ID: {book_id} bo'lgan kitob topilmadi.")


def delete_book(cursor, book_id):
    """
    Delete a specific book from the 'books' table.
    """
    query = "DELETE FROM Books WHERE id = %s"
    cursor.execute(query, (book_id,))
    if cursor.rowcount > 0:
        print(f"Kitob o'chirildi. ID: {book_id}")
    else:
        print(f"ID: {book_id} bo'lgan kitob topilmadi.")


def sort_books_by_year(cursor, order="ASC"):
    """
    Retrieve books sorted by published year.
    """
    query = f"SELECT * FROM Books ORDER BY published_year {order}"
    cursor.execute(query)
    books = cursor.fetchall()
    print("\nKitoblar yil bo'yicha tartiblangan:")
    for book in books:
        print(f"ID: {book[0]}, Nomi: {book[1]}, Yil: {book[3]}, Muallif: {book[2]}")


def count_books(cursor):
    """
    Count the total number of books in the 'books' table.
    """
    cursor.execute("SELECT COUNT(*) FROM Books")
    count = cursor.fetchone()[0]
    print(f"Kutubxonadagi jami kitoblar soni: {count}")


def price_statistics(cursor):
    """
    Display min, max, and average price of books.
    """
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM Books")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"Minimal narx: {min_price}, Maksimal narx: {max_price}, O'rtacha narx: {avg_price:.2f}")
