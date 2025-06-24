# Mon 23 June first created
# Hugh Mortimer
# Used to populate the system with magazines
# Child of Item class

from .item import Item

class Magazine(Item):
    def __init__(self, system:object, itemName:str, available:bool, author:str, issue:int, publishDate, id=None):
        # initialize object
        super().__init__(system, itemName, available, author, id)
        self.issue = issue
        self.publishDate = publishDate
    
    def display_info(self):
        print(f'This {self.__class__.__name__} is called {self.itemName}, created by {self.author}, is issue number {self.issue}, was published on {self.publishDate} and is{' Not' if not self.available else ""} available')