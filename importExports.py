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
        Book(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, author, pages, genre
    elif len(array) == 7:
        Book(system, array[1], bool(array[2]), array[3], array[4], array[5], array[6]) #Item name, available, author, pages, genre, id
    else:
        print(f"Error entering record: {array}")

def create_dvd(array, system):
    if len(array) == 5:
        DVD(system, array[1], bool(array[2]), array[3], array[4]) #Item name, available, duration, director
    elif len(array) == 6:
        DVD(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, duration, director, id
    else:
        print(f"Error entering record: {array}")

def create_magazine(array, system):
    if len(array) == 6:
        Magazine(system, array[1], bool(array[2]), array[3], array[4], array[5]) #Item name, available, author, issue, publish date
    elif len(array) == 7:
        Magazine(system, array[1], bool(array[2]), array[3], array[4], array[5], array[6]) #Item name, available, author, issue, publish date, id
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
    with open("libraryRecords.csv", 'w') as f:
        f.write("Library records exported\n")
        for item in system.records:
            if item.__class__.__name__ == "Item":
                if item.author:
                    f.write(f'Item,{item.itemName},{item.available},{item.author},{item.id}\n')
                else:
                    f.write(f'Item,{item.itemName},{item.available},,{item.id}\n')
            elif item.__class__.__name__ == "Book":
                f.write(f'Book,{item.itemName},{item.available},{item.author},{item.pages},{item.genre},{item.id}\n')
            elif item.__class__.__name__ == "DVD":
                f.write(f'DVD,{item.itemName},{item.available},{item.duration},{item.director},{item.id}\n')
            elif item.__class__.__name__ == "Book":
                f.write(f'Magazine,{item.itemName},{item.available},{item.author},{item.issue},{item.date},{item.id}\n')
            else:
                print(f"Error exporting record {item.name}")