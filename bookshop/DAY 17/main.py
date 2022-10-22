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

with open("id.txt", 'r') as i:
    lines = i.readlines()
    for id in lines:
        data_ids.append(id.strip("\n"))

def add_book():
    book_name = input("\nEnter a book name: ")
    writer_name = input("\nEnter writer name: ")
    time = datetime.today()
    with open("books.txt", 'a') as file:
        if len(ids) == 0:
            with open("id.txt", 'a') as i:
                ids.append('0')
                i.write(f'{str(int(ids[-1]) + 1)}\n')
                data_ids.append('0')
        file.write(f"Book ID: {int(max(data_ids)) + 1} | Book name: {book_name} | Writer: {writer_name} | Added in: {time}\n")
    print("\nAdded succesfuly!")

def show_all(book_list):
    book_count = len(book_list)
    print(f"There are {book_count} books!\n{stars}")
    for line in book_list:
        line = line[:-2]
        book_items = line.split(" | ")
        for item in book_items:
            print(item)
        print(stars)

def show_book():
    book_id = int(input("Enter book ID: "))
    if str(book_id) not in ids:
        print("Wrong input")    
    else:
        for i in book_list:
            if str(book_id) == i[9]:
                deleted_book = "".join(i)
                print(deleted_book)


def remove_book():
    book_id = int(input("Enter book ID: "))
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
                           
with open("id.txt", 'a') as i:
    for line in book_list:
        i.write(f"{line[9]}\n")
        if line[9] not in ids:
            ids.append(line[9])

if word == "add":
    add_book()

if word == "show all":
    show_all(book_list)

if word == "show book":
    show_book()
if word == "remove":
    remove_book()

with open("id.txt", 'a') as i:
    with open("books.txt", 'r') as b:
        b_list = b.readlines()
    for line in b_list:
        i.write(f"{line[9]}\n")
        if line[9] not in ids:
            data_ids.append(line[9])