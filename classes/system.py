# Mon 23 June first created
# Hugh Mortimer
# Used to build the library system

class System:
    def __init__(self, branchName):
        # Initializes library system
        self.name = branchName
        self.idDictionary = {}
        self.nameDictionary = {}
        self.records = []
    
    def newItem(self, itemID:str, itemName:str, itemObject:object):
        # Adds new items to the dictionary
        self.idDictionary[itemID] = itemObject
        self.nameDictionary[itemName] = itemObject
        self.records.append(itemObject)
    
    def printItems(self):
        print(self.nameDictionary)