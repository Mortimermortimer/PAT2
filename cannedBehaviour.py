from classes.system import System
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine
from csvTo2dArray import csvTo2dArray

def create_item(array, system): #turns csv record into base item
    if len(array) == 3:
        Item(system, array[1], bool(array[2])) #Just Item name And if Available
    elif len(array) == 4:
        Item(system, array[1], bool(array[2]), array[3]) #Item name, available, author
    elif len(array) == 5:
        if array[4] == "":
            Item(system, array[1], bool(array[2]), id=array[4]) #Item name, available, id
        else:
            Item(system, array[1], bool(array[2]), array[3], array[4]) #Item name, available, author, id
    else:
        print(f"Error entering record: {array}")

def create_book(array, system):
    if len(array) == 6:
        Item(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, author, pages, genre
    elif len(array) == 7:
        Item(system, array[1], bool(array[2]), array[3], array[4], array[5], array[6]) #Item name, available, author, pages, genre, id
    else:
        print(f"Error entering record: {array}")

def create_dvd(array, system):
    if len(array) == 5:
        Item(system, array[1], bool(array[2]), array[3], array[4]) #Item name, available, duration, director
    elif len(array) == 6:
        Item(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, duration, director, id
    else:
        print(f"Error entering record: {array}")

def create_magazine(array, system):
    if len(array) == 6:
        Item(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, author, issue, publish date
    elif len(array) == 7:
        Item(system, array[1], bool(array[2]), array[3], array[4], array[5], array[6]) #Item name, available, author, issue, publish date, id
    else:
        print(f"Error entering record: {array}")

def batch_import(fileName, system):
    items = csvTo2dArray(fileName)
    for item in items:#sort records by what type they are e.g. item, book, dvd, magazine
        if item[0] == "Item":
            create_item(item, system)
        elif item[0] == "Book":
            create_book(item, system)
        elif item[0] == "DVD":
            create_dvd(item, system)
        elif item[0] == "Magazine":
            create_magazine(item, system)

def export(system):
    for item in system.records:
        pass

epping = System('Epping Library')
batch_import('csvtest.csv', epping)
epping.printItems()