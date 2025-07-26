from classes.system import System
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine
from importExports import batch_import, export
import os

def clear():
    os.system('clear')

epping = System('epping')
mainSys = epping
batch_import(f'{mainSys.name}LibraryRecords.csv', mainSys)

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

def selectTypeAvailable():
    for i, type in enumerate(mainSys.typeDictionary):
        print(f'{i+1}. {type}')
    print(f'{i+2}. View all')
    selection = int(input("Choose a number to continue: ")) #nec
    if selection == len(mainSys.typeDictionary) + 1:
        return mainSys.records
    else:
        for i, type in enumerate(mainSys.typeDictionary):
            if i + 1 == selection:
                return mainSys.typeDictionary[type]

def remove():
    clear()
    print("Remove records") #nec check if there are records at all
    records = selectTypeAvailable()
    clear()
    for i, record in enumerate(records):
        print(f'{i+1}. {record.itemName}')
    selection = int(input("Pick a number to delete: ")) #nec
    if 0 <= selection - 1 < len(records):
        records[selection-1].delete()

def borrow():
    clear()
    print("Borrow") #nec check if there are records at all
    records = selectTypeAvailable()
    clear()
    allClear = False # allClear checks if there is atleast one record to borrow
    for record in records:
        if record.available:
            allClear = True
            break
    if allClear:
        print("🟩 is available to borrow, 🟥 is unavailable\n")
        for i, record in enumerate(records):
            if record.available:
                available = '🟩'
            else:
                available = '🟥'
            print(f'{i+1}. {available} {record.itemName}')
        selection = int(input("Pick a number to borrow: ")) #nec
        clear()
        if 0 <= selection - 1 < len(records):
            records[selection-1].borrow_item()
        input("Press enter to continue")
    else:
        print("No items to borrow")
        for i, record in enumerate(records):
            if record.available:
                available = '🟩'
            else:
                available = '🟥'
            print(f'{i+1}. {available} {record.itemName}')
        input("Press enter to continue")

def returnItem():
    clear()
    print("Return") #nec check if there are records at all
    records = selectTypeAvailable()
    clear()
    allClear = False # allClear checks if there is atleast one record to borrow
    for record in records:
        if record.available == False:
            allClear = True
            break
    if allClear:
        print("🟩 is available to return, 🟥 is unavailable\n")
        for i, record in enumerate(records):
            if record.available:
                available = '🟥'
            else:
                available = '🟩'
            print(f'{i+1}. {available} {record.itemName}')
        selection = int(input("Pick a number to return: ")) #nec
        clear()
        if 0 <= selection - 1 < len(records):
            records[selection-1].return_item()
        input("Press enter to continue")
    else:
        print("No items to return")
        for i, record in enumerate(records):
            if record.available:
                available = '🟥'
            else:
                available = '🟩'
            print(f'{i+1}. {available} {record.itemName}')
        input("Press enter to continue")
    
def search(query:str):
    if query == "":
        clear()
        print("Search by")
        while True:
            selection = input("1. Name\n2. ID\n3. Available\n4. Not Available\nSelect a number to continue: ")
            if selection == '1' or selection == '2' or selection == '3' or selection == '4':
                break
            else:
                clear()
                print("Error, please select a valid option")
        clear()
        if selection == '1':
            selection = input("Search for a record name: ")
            matches = []
            for record in mainSys.records:
                if selection.lower().replace(" ", "") in record.itemName.lower().replace(" ", ""):
                    matches.append(record)
        elif selection == '2':
            selection = input("Search for a record ID: ")
            matches = []
            for record in mainSys.records:
                if selection.lower().replace(" ", "") in record.id.lower().replace(" ", ""):
                    matches.append(record)
        elif selection == '3':
            matches = []
            for record in mainSys.records:
                if record.available:
                    matches.append(record)
        elif selection == '4':
            matches = []
            for record in mainSys.records:
                if record.available == False:
                    matches.append(record)
    else:
        matches = mainSys.records
    clear()
    if len(matches) == 0:#no matches found
        print("No matches found")
        input("Press enter to continue")
        finalMatch = None
    elif len(matches) == 1: #1 match found
        print("1 Match found!")
        finalMatch = matches[0]
    else:#if multiple matches found, select 1
        while True:
            print(f'{len(matches)} Matches found')
            for i, match in enumerate(matches):
                print(f'{i+1}. Name: {match.itemName}')
                print(f'{len(str(len(matches)))*' '}  ID: {match.id}')
                if match.available:
                    available = '🟩'
                else:
                    available = '🟥'
                print(f'{len(str(len(matches)))*' '}  Available: {available}')
            selection = int(input("Select a number to continue: "))#nec
            if 0 <= selection - 1 < len(matches):
                finalMatch = matches[selection-1]
                break
            clear()
            print("Please select a valid number")
    clear()
    if finalMatch:
        if finalMatch.available:
            available = '🟩'
            borrowable = 'Borrow'
        else:
            available = '🟥'
            borrowable = 'Return'
        while True:#action to be taken on final item e.g. borrow, delete etc
            print(f'{available} {finalMatch.itemName}')
            print(f"1. Remove\n2. {borrowable}\n3. See details\n4. Continue to main menu")
            selection = input("Select a number to continue: ")
            clear()
            if selection == '1':
                finalMatch.delete()
                print("Deletion successful")
                input("Press enter to continue")
                break
            elif selection == '2':
                if finalMatch.available:
                    finalMatch.borrow_item()
                else:
                    finalMatch.return_item()
                input("Press enter to continue")
                break
            elif selection == '3':
                clear()
                print(f'Name: {finalMatch.itemName}')
                print(f'Item Type: {finalMatch.__class__.__name__}')
                print(f"ID: {finalMatch.id}")
                print(f"Available: {available}")
                try:
                    if finalMatch.author.strip() != "":
                        print(f"Author: {finalMatch.author}")
                except:
                    pass
                try:
                    print(f"Pages: {finalMatch.pages}")
                except:
                    pass
                try:
                    print(f"Genre: {finalMatch.genre}")
                except:
                    pass
                try:
                    print(f"Duration: {finalMatch.duration}")
                except:
                    pass
                try:
                    print(f"Director: {finalMatch.director}")
                except:
                    pass
                try:
                    print(f"Issue: {finalMatch.issue}")
                except:
                    pass
                try:
                    print(f"Author: {finalMatch.publishDate}")
                except:
                    pass
                input("Press enter to continue")
                break
            elif selection == '4':
                break

while True:
    clear()
    print('1. Add\n2. Remove\n3. Borrow\n4. Return\n5. Search\n6. Catalogue\n7. Exit')
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
        search("")
    elif inp == '6':
        search(" ")
    elif inp == '7':
        export(mainSys)
        break
    elif inp == '8':#Secret dev option, exit without saving
        break
