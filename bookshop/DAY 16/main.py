from sys import argv
from datetime import date
argv.remove("main.py")
word = " ".join(argv)
name_list = word.split(" - ")

if len(name_list) == 2:
    print("Book name:", name_list[0])
    print("Writer:", name_list[1])
    print("Added in:", date.today().strftime("%-d %B %Y"))
else:
    print("Wrong input")