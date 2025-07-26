from classes.system import System
from importExports import batch_import, export                  

epping = System('epping')
mainSys = epping
batch_import(f'{mainSys.name}LibraryRecords.csv', mainSys)
epping.printItems()
export(epping)
