from classes.system import System
from classes.item import Item
from classes.book import Book
from classes.dvd import DVD
from classes.magazine import Magazine

epping = System('Epping')

atomicHabits = Book(epping, "Atomic Habits", True, "James Clear", 300, "Self Improvement")

print(atomicHabits)

atomicHabits.borrow_item()
atomicHabits.borrow_item()
atomicHabits.return_item()
atomicHabits.return_item()
