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
        print(f'Name: {self.itemName}')
        print(f'Item type: Book')
        print(f'ID: {self.id}')
        print(f'Author: {self.author}')
        if self.available:
            print("Available: 🟩")
        else:
            print("Available: 🟥")
        print(f'Pages: {self.pages}')
        print(f'Genre: {self.genre}')