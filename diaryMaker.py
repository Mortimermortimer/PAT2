#Hugh Mortimer
#March 2025
#Program to make diary entries for PAT1 2025, repurposed for PAT2 (preliminary assessment task 2)

import datetime

date = datetime.datetime.now()

def person_Making_Entry(input):
    if input == '':
        return "Hugh Mortimer"
    else:
        return input

person = input("Person Making Entry (Defaults to Hugh Mortimer if left blank): ")
progress = input("Progress since last entry: ")
tasks = input("Tasks achieved: ")
issues = input("Issue(s) encountered: ")
solutions = input("Solution(s): ")
approaches = input("Approaches for upcoming tasks: ")
comments = input("Reflective comments: ")
resources = input("Resources used: ")

diary = open("diary.txt", "a")
diary.write("\n \n")
diary.write(f'{date.strftime("%d")}/{date.strftime("%m")}/{date.strftime("%Y")} {date.strftime("%A")} {date.strftime("%I")}:{date.strftime("%M")} {date.strftime("%p")} \n') #W3 Schools datetime module weschools.com/python/python_datetime.asp
diary.write(f'Person making entry: {person_Making_Entry(person)}\n')
diary.write(f'Progress since last entry: {progress}\n')
diary.write(f'Tasks Achieved: {tasks}\n')
diary.write(f'Issue(s) encountered: {issues}\n')
diary.write(f'Solution(s): {solutions}\n')
diary.write(f'Approaches for upcoming tasks: {approaches}\n')
diary.write(f'Reflective comments: {comments}\n')
diary.write(f'Resources used: {resources}')
diary.close()