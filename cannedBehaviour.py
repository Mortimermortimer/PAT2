from classes.system import System    
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine           
import os
from colorama import Fore, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

input(Fore.GREEN + "Welcome to the canned behaviour, to continue, press enter")
input(Fore.GREEN + "All instructions and comments are in green, outputs from the program are in black")
input(Fore.GREEN + "To begin we first instantsiate a System object")

arden = System('arden')
mainSys = arden

input(Fore.GREEN + "System is created, lets populate it with an item")
print(end="")

elmoToy = Item(mainSys, "Children's Elmo Toy", True)
elmoToy.display_info()

input(Fore.GREEN + "This object is an 'Item', and was automatically assigned an ID")
input(Fore.GREEN + "Let's add some more objects")
print(end="")

book1 = Book(mainSys, "Harry Potter", True, "J.K. Rowling", "200", "Fantasy", "JKR500")
book1.display_info()

input(Fore.GREEN + "This object comes from the Book class, and this time we assigned it an ID")
input(Fore.GREEN + "The Book class inherits from the Item class. DVD and Magazine also do this")
input(Fore.GREEN + "These three child classes use polymorphism to change the methods encapsulated in the object")
input(Fore.GREEN + "You can see when the Book displayed it's info it was able to display more specific information")

input(Fore.GREEN + "Let's try borrowing it now")

print(end="")
book1.borrow_item()

input(Fore.GREEN + "Let's have a look at it's status")

print(end="")
book1.display_info()

input(Fore.GREEN + "Now let's see what happens if we try borrow it again")

print(end="")
book1.borrow_item()

input(Fore.GREEN + "Isn't that clever, let's make sure the availability status is still correct")

print(end="")
book1.display_info()

input(Fore.GREEN + "Let's have a look at all the records now")

print(end="")
mainSys.printItems()

input(Fore.GREEN + "How about some more detail")

print(end="")
mainSys.detailedPrintItems()

input(Fore.GREEN + "Let's add some more records")

print(end="")
Book(mainSys, "Atomic Habits", True, "James Clear", 230, "Self Improvement")
Magazine(mainSys, "NYT Daily Paper", True, "Josh Smart", 479371, "Sun 20 July 2025")
DVD(mainSys, "Ocean's 11", True, "2h 11m", "Steven Sodherburg")
Book(mainSys, "The art of war", True, "Sun Tzu", 150, "Historical")
Magazine(mainSys, "NYT Daily Paper", True, "Josh Smart", 479372, "Mon 21 July 2025")
Magazine(mainSys, "NYT Daily Paper", True, "Emily Smith", 479373, "Tue 22 July 2025")
DVD(mainSys, "Oppenheimer", True, "3h", "Christopher Nolan")
DVD(mainSys, "Parasite", True, "2h 30m", "Bong Joon Ho")
Item(mainSys, "Whiteboard", True)
Item(mainSys, "Hamster", True)

input(Fore.GREEN + "And let's borrow a few of them")

print(end="")
mainSys.records[5].borrow_item()
mainSys.records[2].borrow_item()
mainSys.records[8].borrow_item()
mainSys.records[10].borrow_item()

input(Fore.GREEN + "Now let's have an overview of what the library has to offer")

print(end="")
mainSys.availabilityPrint()

input(Fore.GREEN + "For more in depth searches, such as query by name, ID and availability, use the full interactive version found at libraryEditor.py")

input(Fore.GREEN + "And that's just a quick overview of the system\nFor a more detailed look, try out the CLI on the libraryEditor.py page\nThere are many more features to try out there")