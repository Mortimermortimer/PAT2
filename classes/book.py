# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with books
# Child of Item class

from .item import Item

class Book(Item):
    def __init__(self, system:object, itemName:str, available:bool, author:str, pages:int, genre:str, id=None):
        # initialize object
        super().__init__(system, itemName, available, author, id)
        self.pages = pages
        self.genre = genre
    
    def display_info(self):
        print(f'This book is called {self.itemName}, written by {self.author}, is in genre {self.genre}, {self.pages} long and is{' Not' if not self.available else ""} available')