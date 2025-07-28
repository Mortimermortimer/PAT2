PAT2
Preliminary Course Assessment task 2 2025 - Library System

This file contains
1. Class Explanations
2. File Explanations
3. User Instructions
4. Class Heirarchy
5. Canned Behaviour output


# #
# //
# 1. Class Explanations
# //
# #

#
# System
#

Overview
System runs the library system. For each library branch there is e.g. arden library, epping library, a new system object is instantsiated. It houses all of the dictionaries holding all objects.

Functions
init - initializes the system
newItem - adds a new item created in the system to all of the dictionaries
printItems - prints the {Name: Object location} dictionary

#
# Item
#

Overview
Item is the Parent class of all items, it is parent to Book, DVD, Magazine. Items populate the library with objects.

Functions
init - initializes the system, if an ID is not provided, one will be created for it. Uses the systems function newItem
str - magic method that returns data about the item
display_info - Displays some info about the item
borrow_item - sets the items available state to false if possible, otherwise throws error
return_item - sets the items available state to true if possible, otherwise throws error
delete - deletes item from all dictionaries and lists in the system

#
# Book, DVD, Magazine
#

Overview
All these classes do the same thing, but with slightly different attributes. They are all child to Item.

Functions
init - Initializes by using the super method, which INHERITS the Item class, then adds the other specific attributes
display_info - uses POLYMORPHISM to override the parent class and display more specific info about the item

# #
# //
# 2. File Explanations
# //
# #

#
# cannedBehaviour.py
#

Overview
Runs step by step procedural code that demonstrates the features of the program

#
# csvTo2dArray.py
#

Overview
Used by other files, it contains a helper function that converts a csv into a 2d array, making it easier to work with

#
# eppingLibraryRecords.csv
#

Overview
Sample database used by libraryEditor.py, contains pre populated items

#
# importsExports.py
#

Overview
Uses a csv to instantsiate objects, used as a helper function. Also exports instantiated objects to a csv

#
# key.txt
#

Overview
Key for how different objects are stored in the database

#
# libraryEditor.py
#

Overview
Runs the CLI - which is used to edit the library

# #
# //
# 3. User Instructions
# //
# #

#
# cannedBehaviour.py
#

Run the program, read the terminal, when ready for next step, press enter. All instructions are in green, and system output is black

#
# libraryEditor.py
#

Run the program
Select your action by entering the corresponding number
Follow further instructions
At the end press 7 to save and exit
At any point - press enter to cancel

# #
# //
# 4. Class Heirarchy
# //
# #

System is needed for Item, but item does not inherit from system.

           System

            Item
             |
             |
             |
            \ /
    Book, DVD, Magazine

# #
# //
# 5. Canned Behaviour Output
# // 
# #

**For a coloured version (recommended) - please run the file**

Welcome to the canned behaviour, to continue, press enter
All instructions and comments are in green, outputs from the program are in black
To begin we first instantsiate a System object
System is created, lets populate it with an item
Name: Children's Elmo Toy
Item type: Item
ID: ALI1
Available: 🟩
This object is an 'Item', and was automatically assigned an ID
Let's add some more objects
Name: Harry Potter
Item type: Book
ID: JKR500
Author: J.K. Rowling
Available: 🟩
Pages: 200
Genre: Fantasy
This object comes from the Book class, and this time we assigned it an ID
The Book class inherits from the Item class. DVD and Magazine also do this
These three child classes use polymorphism to change the methods encapsulated in the object
You can see when the Book displayed it's info it was able to display more specific information
Let's try borrowing it now
Harry Potter has been successfully borrowed
Let's have a look at it's status
Name: Harry Potter
Item type: Book
ID: JKR500
Author: J.K. Rowling
Available: 🟥
Pages: 200
Genre: Fantasy
Now let's see what happens if we try borrow it again
This item is not available
Isn't that clever, let's make sure the availability status is still correct
Name: Harry Potter
Item type: Book
ID: JKR500
Author: J.K. Rowling
Available: 🟥
Pages: 200
Genre: Fantasy
Let's have a look at all the records now
{"Children's Elmo Toy": <classes.item.Item object at 0x7ac30c4f3170>, 'Harry Potter': <classes.book.Book object at 0x7ac30c4f3a70>}
How about some more detail
Name: Children's Elmo Toy
Item type: Item
ID: ALI1
Available: 🟩

Name: Harry Potter
Item type: Book
ID: JKR500
Author: J.K. Rowling
Available: 🟥
Pages: 200
Genre: Fantasy

Let's add some more records
And let's borrow a few of them
The art of war has been successfully borrowed
Atomic Habits has been successfully borrowed
Oppenheimer has been successfully borrowed
Whiteboard has been successfully borrowed
Now let's have an overview of what the library has to offer
🟩 Children's Elmo Toy
🟥 Harry Potter
🟥 Atomic Habits
🟩 NYT Daily Paper
🟩 Ocean's 11
🟥 The art of war
🟩 NYT Daily Paper
🟩 NYT Daily Paper
🟥 Oppenheimer
🟩 Parasite
🟥 Whiteboard
🟩 Hamster
For more in depth searches, such as query by name, ID and availability, use the full interactive version found at libraryEditor.py
And that's just a quick overview of the system
For a more detailed look, try out the CLI on the libraryEditor.py page
There are many more features to try out there

# #
# //
# 6. Other Outputs
# //
# #

# Catalogue


20 Matches found
1. Name: Library Guide to Cataloging
    ID: ELI1
    Available: 🟩
2. Name: How Libraries Work
    ID: ELI2
    Available: 🟩
3. Name: Public Library Handbook
    ID: ELI3
    Available: 🟥
4. Name: Digital Archiving Basics
    ID: ELI4
    Available: 🟩
5. Name: Community and Literacy
    ID: ELI5
    Available: 🟩
6. Name: The Last Time We Spoke
    ID: ELI6
    Available: 🟩
7. Name: Coding for Kids
    ID: ELI7
    Available: 🟩
8. Name: History of the Silk Road
    ID: ELI8
    Available: 🟥
9. Name: Poems from the Outback
    ID: ELI9
    Available: 🟩
10. Name: Modern Architecture
    ID: ELI10
    Available: 🟥
11. Name: Planet Earth: Oceans
    ID: ELI11
    Available: 🟩
12. Name: The Grand Heist
    ID: ELI12
    Available: 🟩
13. Name: Cooking Masterclass
    ID: ELI13
    Available: 🟩
14. Name: Learn Tai Chi
    ID: ELI14
    Available: 🟩
15. Name: Kids Sing-Along
    ID: ELI15
    Available: 🟩
16. Name: Science Monthly
    ID: ELI16
    Available: 🟥
17. Name: Australian Fiction Weekly
    ID: ELI17
    Available: 🟥
18. Name: Nature & You
    ID: ELI18
    Available: 🟩
19. Name: Tech Tinker
    ID: ELI19
    Available: 🟩
20. Name: Global Gardens
    ID: ELI20
    Available: 🟥

Select a number to continue:

# Search

Search by
1. Name
2. ID
3. Available
4. Not Available
Select a number to continue: 

# Create

Create new records
1. Item
2. Book
3. DVD
4. Magazine
Choose a number to continue: 

# Remove

Remove records
1. Item
2. Book
3. DVD
4. Magazine
5. View all
Choose a number to continue: 

# Main menu

1. Add
2. Remove
3. Borrow
4. Return
5. Search
6. Catalogue
7. Exit
Choose a number to continue: 
