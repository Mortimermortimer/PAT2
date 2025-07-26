# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with items
# Parent to book, magazine and DVD classes

import random
from .system import System

class Item():
    def __init__(self, system:object, itemName:str, available:bool, author=None, id=None):
        # initialize object
        self.itemName = itemName
        self.available = available
        self.author = author
        self.system = system

        # Create id if there isn't one already
        if id:
            self.id = id
        else:
            self.id = f'{system.name[0].upper()}LI{system.maxid+1}'
        
        # import the newly made object into the system
        System.newItem(system, self.id, self.itemName, self)
    
    def __str__(self):
        return(f'Item type: {self.__class__.__name__}\nItem Name: {self.itemName}\nID: {self.id}')

    def display_info(self):
        print(f'Item')
        print(self.name)
        if self.author:
            print(self.author)
        if self.available:
            print("🟩 Available to borrow")
        else:
            print("🟥 Unavailable to borrow")
    
    def borrow_item(self):
        if self.available:
            self.available = False
            print(f'{self.itemName} has been successfully borrowed')
        else:
            print(f"This item is not available")
    
    def return_item(self):
        if not self.available:
            self.available = True
            print(f'{self.itemName} has been successfully returned')
        else:
            print(f"This item has not been borrowed")
    
    def delete(self):
        self.system.idDictionary.pop(self.id, None)
        self.system.nameDictionary.pop(self.itemName, None)
        item_type = self.__class__.__name__
        if item_type in self.system.typeDictionary:
            if self in self.system.typeDictionary[item_type]:
                self.system.typeDictionary[item_type].remove(self)