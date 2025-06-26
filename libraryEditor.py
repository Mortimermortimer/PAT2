from classes.system import System
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine
from importExports import batch_import, export
import os

def clear():
    os.system('clear')

epping = System('Epping Library')
batch_import('libraryRecords.csv', epping)
mainSys = epping

def add():
    clear()
    while True:
        print("Create new records")
        print('1. Item\n2. Book\n3. DVD\n4. Magazine\n5. Return to main menu')
        inp = input("Choose a number to continue: ")
        if inp == '1':
            clear()
            print("Create new Item")
            name = input("What is it called: ")
            author = input("Who is the author/creator (leave blank if none): ")
            if author != "":
                Item(mainSys, name, True, author)
            else:
                Item(mainSys, name, True)
            clear()
            print(f"New item created called {name}")
        elif inp == '2':
            clear()
            print("Create new Book")
            name = input("What is it called: ")
            author = input("Who is the author: ")
            pages = int(input("How many pages does it have: ")) #nec
            genre = input("What genre is it: ")
            Book(mainSys, name, True, author, pages, genre)
            clear()
            print(f"New book created called {name}")
        elif inp == '3':
            clear()
            print("Create new DVD")
            name = input("What is it called: ")
            duration = input("How long does it run for: ")
            director = input("Who is the director: ")
            DVD(mainSys, name, True, duration, director)
            clear()
            print(f"New DVD created called {name}")
        elif inp == '4':
            clear()
            print("Create new Magazine")
            name = input("What is it called: ")
            author = input("Who is the author: ")
            issue = int(input("What issue no. is it: ")) #nec
            publish = input("When was it published: ")
            Book(mainSys, name, True, author, issue, publish)
            clear()
            print(f"New magazine created called {name}")
        elif inp == '5':
            break
        else:
            clear()

def remove():
    pass

def borrow():
    pass

def returnItem():
    pass

while True:
    clear()
    print('1. Add\n2. Remove\n3. Borrow\n4. Return\n5. Exit')
    inp = input("Choose a number to continue: ")
    if inp == '1':
        add()
    elif inp == '2':
        remove()
    elif inp == '3':
        borrow()
    elif inp == '4':
        returnItem()
    elif inp == '5':
        break