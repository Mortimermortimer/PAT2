# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with DVD's
# Child of Item class

from .item import Item

class DVD(Item):
    def __init__(self, system:object, itemName:str, available:bool, duration, director, id=None):
        # initialize object
        super().__init__(system, itemName, available, id=id)
        self.duration = duration
        self.director = director
    
    def display_info(self):
        print(f'Name: {self.itemName}')
        print(f'Item type: DVD')
        print(f'ID: {self.id}')
        print(f'Author: {self.author}')
        if self.available:
            print("Available: 🟩")
        else:
            print("Available: 🟥")
        print(f'Duration: {self.duration}')
        print(f'Director: {self.director}')