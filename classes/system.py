# Mon 23 June first created
# Hugh Mortimer
# Used to build the library system

class System:
    def __init__(self, branchName):
        # Initializes library system
        self.name = branchName
        self.idDictionary = {} #stores {ID: Object location}
        self.nameDictionary = {} #stores {Name: Object location}
        self.typeDictionary = {} #stores {Item type: Object location}
        self.records = []
        self.maxid = 0
    
    def newItem(self, itemID:str, itemName:str, itemObject:object):
        # Adds new items to the dictionaries
        self.idDictionary[itemID] = itemObject
        self.nameDictionary[itemName] = itemObject
        if itemObject.__class__.__name__ in self.typeDictionary:
            self.typeDictionary[itemObject.__class__.__name__].append(itemObject)
        else:
            self.typeDictionary[itemObject.__class__.__name__] = [itemObject]
        self.records.append(itemObject)
        self.maxid += 1
    
    def printItems(self):
        print(self.nameDictionary)

    def detailedPrintItems(self):
        for item in self.records:
            item.display_info()
            print()
    
    def availabilityPrint(self):
        for item in self.records:
            if item.available:
                print(f'🟩 {item.itemName}')
            else:
                print(f'🟥 {item.itemName}')
    