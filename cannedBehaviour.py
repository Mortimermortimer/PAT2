from classes.system import System
from importExports import batch_import, export                  

epping = System('Epping Library')
batch_import('libraryRecords.csv', epping)
epping.printItems()
export(epping)
