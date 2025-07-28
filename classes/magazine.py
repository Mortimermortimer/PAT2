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
        print(f'Name: {self.itemName}')
        print(f'Item type: Magazine')
        print(f'ID: {self.id}')
        print(f'Author: {self.author}')
        if self.available:
            print("Available: 🟩")
        else:
            print("Available: 🟥")
        print(f'Issue: {self.issue}')
        print(f'Publish Date: {self.publishDate}')