import pymysql.cursors
from sys import argv
from datetime import datetime
argv.remove("main.py")
word = " ".join(argv)
# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='12345',
                             database='BookShop',
                             cursorclass=pymysql.cursors.DictCursor)


def create_table():

    with connection.cursor() as cursor:
        sql = """
            create table if not exists Book_info(
            id int unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
            title varchar(255) NOT NULL,
            author varchar(255) NOT NULL,
            published_at date,
            exist boolean DEFAULT TRUE,
            genre varchar(255),
            price DECIMAL(6, 2) DEFAULT 10.00
        );
        """
        cursor.execute(sql)
    connection.commit()
    print("Worked")


def create_book(book_name, author_name, published_at, exist, genre, price):
    
    with connection.cursor() as cursor:
        sql = """
            insert into Book_info (title, author, published_at, exist, genre, price) values
            (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (book_name, author_name, published_at, exist, genre, price))
    connection.commit()
    print("Worked")


def show_all():
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def show_book(id):
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info where id = %s;
        """
        cursor.execute(sql, id)
        result = cursor.fetchone()
    return result


def change_status(id):
    with connection.cursor() as cursor:
        sql = """
            select exist from Book_info where id = %s;
        """
        cursor.execute(sql, id)
        result = cursor.fetchone()["exist"]
    if result == 1:
        with connection.cursor() as cursor:
            sql = """
                UPDATE Book_info SET exist = CASE WHEN id = %s THEN false ELSE exist END
            """
            cursor.execute(sql, id)
        connection.commit()
    else:
        with connection.cursor() as cursor:
            sql = """
                UPDATE Book_info SET exist = CASE WHEN id = %s THEN true ELSE exist END
            """
            cursor.execute(sql, id)
        connection.commit()


def change_price(id, new_price):
    with connection.cursor() as cursor:
        sql = """
            UPDATE Book_info SET price = CASE WHEN id = %s THEN %s ELSE price END
        """
        cursor.execute(sql, (id, new_price))
    connection.commit()
    print("Worked")


def remove(id):
    with connection.cursor() as cursor:
        sql = """
            DELETE FROM Book_info WHERE id = %s;
        """
        cursor.execute(sql, id)
    connection.commit()
    print("Worked")


def search(wanted_word):
    with connection.cursor() as cursor:
        sql = """
            select * from Book_info;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    for book in result:
        if wanted_word in book["title"].lower():
            print(book)            

        if wanted_word in book["author"].lower():
            print(book)




if word.lower() == "add table":
    create_table()
    print(word)

if word.lower() == "add book":
    book_name = input("Enter a book name: ")
    author_name = input("Enter a book's author: ")
    published_at = datetime.now()
    exist = True
    genre = input("Enter a book's genre: ")
    price = float(input("Enter price of book: "))
    create_book(book_name, author_name, published_at, exist, genre, price)
    print(word)

if word.lower() == "show all":
    for book in show_all():
        print(book)

if word.lower() == "show book":
    id = int(input("Enter book id: "))
    print(show_book(id))

if word.lower() == "change status":
    id = int(input("Enter a book id: "))
    change_status(id)

if word.lower() == "change price":
    id = int(input("Enter a book id: "))
    new_price = float(input("Enter new price of book: "))
    change_price(id, new_price)

if word.lower() == "remove":
    id = int(input("Enter book id: "))
    remove(id)

if word.lower() == "search":
    wanted_word = input("Enter a word: ").lower()
    search(wanted_word)


