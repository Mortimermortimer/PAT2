# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with items
# Parent to book, magazine and DVD classes

import random
from .system import System

class Item():
    def __init__(self, system:object, itemName:str, available:bool, author=None, id=None):
        # initialize object
        self.name = itemName
        self.available = available
        self.author = author

        # Create id if there isn't one already
        if id:
            self.id = id
        else:
            self.id = str(random.randint(000000000,999999999))
        
        # import the newly made object into the system
        System.newItem(system, self.id, self.name, self)