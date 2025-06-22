# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with DVD's
# Child of Item class

from .item import Item

class DVD(Item):
    def __init__(self, system:object, itemName:str, available:bool, author:str, duration, director, id=None):
        # initialize object
        super().__init__(system, itemName, available, author, id)
        self.duration = duration
        self.director = director