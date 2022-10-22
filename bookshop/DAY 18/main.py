b = open("books.txt", 'r')
from sys import argv
from datetime import datetime
msg = argv
msg.remove("main.py")
word = " ".join(msg)
book_list = b.readlines() 
stars = "*************************************"
b.close()
ids = []
data_ids = []

class Book:

    def __init__(self, title, author, id, date):
        self.title = title
        self.author = author
        self.id = id
        self.date = date
    
    with open("id.txt", 'r') as i:
        lines = i.readlines()
        for id in lines:
            data_ids.append(id.strip("\n"))

    def add_book(self, author, title, date):
        self.author = author
        self.title = title
        self.date = date
        with open("books.txt", 'a') as file:
            if len(ids) == 0:
                with open("id.txt", 'a') as i:
                    ids.append('0')
                    i.write(f'{str(int(ids[-1]) + 1)}\n')
                    data_ids.append('0')
            file.write(f"Book ID: {int(max(data_ids)) + 1} | Book name: {author} | Writer: {title} | Added in: {date}\n")
        print("\nAdded succesfuly!")
    def show_all(self, book_list):
        book_count = len(book_list)
        print(f"There are {book_count} books!\n{stars}")
        for line in book_list:
            line = line[:-2]
            book_items = line.split(" | ")
            for item in book_items:
                print(item)
            print(stars)
    def show_book(self, book_id):
        if str(book_id) not in ids:
            print("Wrong input")    
        else:
            for i in book_list:
                if str(book_id) == i[9]:
                    show_book = "".join(i)
                    print(show_book)
    def remove_book(self, book_id):
        if str(book_id) not in ids:
            print("Wrong input")    
        else:
            ids.remove(str(book_id))
            for i in book_list:
                if str(book_id) == i[9]:
                    deleted_book = "".join(i)
                    with open("books.txt", 'w') as f:
                        for line in book_list:
                            if line != deleted_book:
                                f.write(line)
            print("\nDeleted succesfuly!")
    def set_date(self, book_id):
        if str(book_id) not in ids:
            print("Wrong input") 
        else:
            for i in book_list:
                if str(book_id) == i[9]:
                    deleted_book = "".join(i)
                    with open("books.txt", 'w') as f:
                        for line in book_list:
                            if line != deleted_book:
                                f.write(line)
                    book_items = deleted_book.split(" | ")
                    book_name = book_items[1][11:]
                    book_writer = book_items[2][8:]
                    added_date = datetime.now()
                    with open("books.txt", 'a') as f:
                        f.write(f"Book ID: {book_id} | Book name: {book_name} | Writer: {book_writer} | Added in: {added_date}\n")
            print("Changed succesfuly!")


with open("id.txt", 'a') as i:
    for line in book_list:
        i.write(f"{line[9]}\n")
        if line[9] not in ids:
            ids.append(line[9])

book = Book("dfds","sdf",1,123)

if word == "add":
    author = input("Enter a book name:\n")
    title = input("\nEnter a writer name:\n")
    time = datetime.today()
    book.add_book(author, title, time)

if word == "show all":
    book.show_all(book_list)

if word == "show book":
    book_id = int(input("Enter a book id: "))
    book.show_book(book_id)
if word == "remove":
    book_id = int(input("Enter a book id: "))
    book.remove_book(book_id)
if word == "set date":
    book_id = int(input("Enter a book id: "))
    book.set_date(book_id)

with open("id.txt", 'a') as i:
    with open("books.txt", 'r') as b:
        b_list = b.readlines()
    for line in b_list:
        i.write(f"{line[9]}\n")
        if line[9] not in ids:
            data_ids.append(line[9])