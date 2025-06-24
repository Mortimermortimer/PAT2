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
        print(f'This {self.__class__.__name__} is called {self.itemName}, directed by {self.director}, is {self.duration} long and is{' Not' if not self.available else ""} available')