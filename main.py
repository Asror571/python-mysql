import mysql.connector
import setting
from db import (
    create_books_table,
    insert_book,
    show_all_books,
    search_books_by_author_or_genre,
    update_book_price,
    update_book_availability,
    delete_book,
    sort_books_by_year,
    count_books,
    price_statistics,
)

def main():
    connection = mysql.connector.connect(
        host=setting.host,
        user=setting.user,
        password=setting.password,
        port=setting.port
    )

    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {setting.db_name}")
    cursor.execute(f"USE {setting.db_name}")

    create_books_table(cursor)

    while True:
        print("""
        1. Kitob qo'shish
        2. Barcha kitoblarni ko'rsatish
        3. Muallif yoki janr bo'yicha qidirish
        4. Kitob narxini yangilash
        5. Kitob mavjudligini o'zgartirish
        6. Kitobni o'chirish
        7. Yil bo'yicha tartiblash
        8. Kitoblar sonini hisoblash
        9. Narx bo'yicha statistika
        0. Chiqish
        """)
        command = input("Tanlang: ")
        if command == "1":
            title = input("Kitob nomi: ")
            author = input("Muallif: ")
            year = int(input("Yaratilgan yil: "))
            genre = input("Janr: ")
            price = int(input("Narx: "))
            available = input("Mavjudmi  : ").lower() == "ha"
            insert_book(cursor, title, author, year, genre, price, available)
            connection.commit()
        elif command == "2":
            show_all_books(cursor)
        elif command == "3":
            search_type = input("Qidiruv turi : ").lower()
            search_value = input("Qidiruv qiymati: ")
            search_books_by_author_or_genre(cursor, search_type, search_value)
        elif command == "4":
            book_id = int(input("Kitob ID: "))
            new_price = int(input("Yangi narx: "))
            update_book_price(cursor, book_id, new_price)
            connection.commit()
        elif command == "5":
            book_id = int(input("Kitob ID: "))
            available = input("Mavjudmi? (ha/yo'q): ").lower() == "ha"
            update_book_availability(cursor, book_id, available)
            connection.commit()
        elif command == "6":
            book_id = int(input("Kitob ID: "))
            delete_book(cursor, book_id)
            connection.commit()
        elif command == "7":
            order = input("Tartib (ASC/DESC): ").upper()
            sort_books_by_year(cursor, order)
        elif command == "8":
            count_books(cursor)
        elif command == "9":
            price_statistics(cursor)
        elif command == "0":
            break
        else:
            print("Siz kiritgan buyruq mavjud emas")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
