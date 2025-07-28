from classes.system import System
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine
from importExports import batch_import, export
import os

def clear():#Clears the screen for both Windows and Mac
    os.system('cls' if os.name == 'nt' else 'clear')

epping = System('epping')#creates system
ryde = System('ryde')#Secondary system - for if you would like to test with a blank slate
mainSys = epping
#mainSys = ryde
'''Uncomment Line above to trial with secondary system'''
try:
    batch_import(f'{mainSys.name}LibraryRecords.csv', mainSys)#Imports records from csv file
except:
    pass

def intInput(text: str):#Takes input and handles any invalid inputs
    while True:
        result = input(text)
        if result == "":
            return 'User has decided to skip'
        try:
            result = int(result)
            return result
        except:
            clear()
            print("Invalid input, please try again")

def add():#Adds records to database
    clear()
    while True:
        print("Create new records")
        print('1. Item\n2. Book\n3. DVD\n4. Magazine')
        inp = input("Choose a number to continue: ")
        if inp == '1':#For creating items
            clear()
            print("Create new Item")
            name = input("What is it called: ")
            if name != "":
                author = input("Who is the author/creator (leave blank if none): ")
                if author != "":
                    Item(mainSys, name, True, author)
                else:
                    Item(mainSys, name, True)
                clear()
                print(f"New item created called {name}")
                break
            else:
                clear()
                break
        elif inp == '2':#For creating books
            clear()
            print("Create new Book")
            name = input("What is it called: ")
            if name != "":
                author = input("Who is the author: ")
                pages = intInput("How many pages does it have: ") #nec
                genre = input("What genre is it: ")
                Book(mainSys, name, True, author, pages, genre)
                clear()
                print(f"New book created called {name}")
                break
            else:
                clear()
                break
        elif inp == '3':#For creating DVDs
            clear()
            print("Create new DVD")
            name = input("What is it called: ")
            if name != "":
                duration = input("How long does it run for: ")
                director = input("Who is the director: ")
                DVD(mainSys, name, True, duration, director)
                clear()
                print(f"New DVD created called {name}")
                break
            else:
                clear()
                break
        elif inp == '4':#For creating magazines
            clear()
            print("Create new Magazine")
            name = input("What is it called: ")
            if name != "":
                author = input("Who is the author: ")
                issue = intInput("What issue no. is it: ") #nec
                publish = input("When was it published: ")
                Magazine(mainSys, name, True, author, issue, publish)
                clear()
                print(f"New magazine created called {name}")
                break
            else:
                clear()
                break
        elif inp == '5' or inp == '':#Cancel
            break
        else:
            clear()
            print("Invalid input, please try again")

def selectTypeAvailable():#Function used by other functions, gets user to select type of item they want to interact with
    if len(mainSys.records) == 0:
        return 'No records'
    totalText = ''
    for i, type in enumerate(mainSys.typeDictionary):
        totalText += f'{i+1}. {type}\n'
    totalText += f'{i+2}. View all'
    selection = intInput(f"{totalText}\nChoose a number to continue: ")
    if selection == "User has decided to skip":
        return "User has decided to skip"
    if selection == len(mainSys.typeDictionary) + 1:
        return mainSys.records
    else:
        for i, type in enumerate(mainSys.typeDictionary):
            if i + 1 == selection:
                return mainSys.typeDictionary[type]

def remove():#used to remove records from system
    clear()
    print("Remove records")
    records = selectTypeAvailable()
    if records == 'User has decided to skip':
        return 'User has decided to skip'
    elif records == "No records":
        input("No records to remove, press enter to continue")
        return 'No records'
    if len(records) == 0:
        clear()
        print("No records")
    else:
        clear()
        totalText = ''
        for i, record in enumerate(records):
            totalText += f'{i+1}. {record.itemName}\n'
        selection = intInput(f"{totalText}\nPick a number to delete: ") #nec
        if selection == "User has decided to skip":
            return "User has decided to skip"
        if 0 <= selection - 1 < len(records):
            records[selection-1].delete()

def borrow():#Borrows books
    clear()
    print("Borrow")
    records = selectTypeAvailable()
    clear()
    if records == 'User has decided to skip':
        return 'User has decided to skip'
    elif records == 'No records':
        input("No records to borrow, press enter to continue")
        return
    allClear = False # allClear checks if there is atleast one record to borrow
    for record in records:
        if record.available:
            allClear = True
            break
    if allClear:
        while True:#Next section displays all available books to borrow 
            totalText = "🟩 is available to borrow, 🟥 is unavailable\n"
            for i, record in enumerate(records):
                if record.available:
                    available = '🟩'
                else:
                    available = '🟥'
                totalText += f'{i+1}. {available} {record.itemName}\n'
            selection = intInput(f"{totalText}\n\nPick a number to borrow: ") #nec
            clear()
            if selection == "User has decided to skip":
                return "User has decided to skip"
            if 0 <= selection - 1 < len(records):
                records[selection-1].borrow_item()#This line borrows the book
                input("Press enter to continue")
                break
            print("Please enter a valid number")
    else:
        print("No items to borrow")
        for i, record in enumerate(records):
            if record.available:
                available = '🟩'
            else:
                available = '🟥'
            print(f'{i+1}. {available} {record.itemName}')
        input("Press enter to continue")

def returnItem():#Returns items
    clear()
    print("Return")
    records = selectTypeAvailable()
    clear()
    if records == "User has decided to skip":
        return "User has decided to skip"
    elif records == 'No records':
        input("No records to borrow, press enter to continue")
        return
    allClear = False # allClear checks if there is atleast one record to borrow
    for record in records:
        if record.available == False:
            allClear = True
            break
    if allClear:
        while True:#Shows which items are available to return
            totalText = "🟩 is available to return, 🟥 is unavailable\n"
            for i, record in enumerate(records):
                if record.available:
                    available = '🟥'
                else:
                    available = '🟩'
                totalText += f'{i+1}. {available} {record.itemName}\n'
            selection = intInput(f"{totalText}\nPick a number to return: ") #nec
            clear()
            if selection == "User has decided to skip":
                return "User has decided to skip"
            if 0 <= selection - 1 < len(records):
                records[selection-1].return_item()#This line returns the item
                input("Press enter to continue")
                break
            print("Invalid input, please try again")
    else:
        print("No items to return")
        for i, record in enumerate(records):
            if record.available:
                available = '🟥'
            else:
                available = '🟩'
            print(f'{i+1}. {available} {record.itemName}')
        input("Press enter to continue")
    
def search(query:str):#Searches and sorts books based on user query
    skip = False #when skip is true it will return the user to main menu
    if query == "":
        clear()
        print("Search by")
        while True:
            selection = input("1. Name\n2. ID\n3. Available\n4. Not Available\nSelect a number to continue: ")
            if selection == '1' or selection == '2' or selection == '3' or selection == '4' or selection == '':
                break
            else:
                clear()
                print("Error, please select a valid option")
        clear()
        if selection == '1':#Search by name
            selection = input("Search for a record name: ")
            matches = []
            for record in mainSys.records:
                if selection.lower().replace(" ", "") in record.itemName.lower().replace(" ", ""):
                    matches.append(record)
        elif selection == '2':#Search by ID
            selection = input("Search for a record ID: ")
            matches = []
            for record in mainSys.records:
                if selection.lower().replace(" ", "") in record.id.lower().replace(" ", ""):
                    matches.append(record)
        elif selection == '3':#Search by available
            matches = []
            for record in mainSys.records:
                if record.available:
                    matches.append(record)
        elif selection == '4':#search by not available
            matches = []
            for record in mainSys.records:
                if record.available == False:
                    matches.append(record)
        elif selection == '':
            return
    else:
        matches = mainSys.records#This is where the catalogue feature starts from - it views all records
    clear()
    if skip == True:
        finalMatch = None
        return
    elif len(matches) == 0:#no matches found - goes to main menu after this
        print("No matches found")
        input("Press enter to continue")
        return
    elif len(matches) == 1: #1 match found
        print("1 Match found!")
        finalMatch = matches[0]
    else:#if multiple matches found, select 1
        while True:
            totalText = f'{len(matches)} Matches found\n'
            for i, match in enumerate(matches):
                totalText += f'{i+1}. Name: {match.itemName}\n'
                totalText += f'{len(str(len(matches)))*' '}  ID: {match.id}\n'
                if match.available:
                    available = '🟩'
                else:
                    available = '🟥'
                totalText += f'{len(str(len(matches)))*' '}  Available: {available}\n'
            selection = intInput(f"{totalText}\nSelect a number to continue: ")#nec
            if selection == "User has decided to skip":
                return "User has decided to skip"
            if 0 <= selection - 1 < len(matches):
                finalMatch = matches[selection-1]
                break
            clear()
            print("Please select a valid number")
    clear()
    if finalMatch.available:
        available = '🟩'
        borrowable = 'Borrow'
    else:
        available = '🟥'
        borrowable = 'Return'
    while True:#action to be taken on final item e.g. borrow, delete etc
        print(f'{available} {finalMatch.itemName}')
        print(f"1. Remove\n2. {borrowable}\n3. See details")
        selection = input("Select a number to continue: ")
        clear()
        if selection == '1':#Delete record
            finalMatch.delete()
            print("Deletion successful")
            input("Press enter to continue")
            break
        elif selection == '2':#Borrow or return record - automatically adjusts depending on availability
            if finalMatch.available:
                finalMatch.borrow_item()
            else:
                finalMatch.return_item()
            input("Press enter to continue")
            break
        elif selection == '3':#Shows all attributes
            clear()
            finalMatch.display_info()
            input("Press enter to continue")
            break
        elif selection == '4' or selection == '':
            break

while True:#Main menu loop
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
