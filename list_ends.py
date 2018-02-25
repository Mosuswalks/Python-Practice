"""
Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new list 
of only the first and last elements of the given list.

For practice, write this code inside a function.
"""
list = [7,5,3,5,4,2,9,8]

def listEnds(list):
    newList = [list[0], list[-1]]
    return newList
    
print(listEnds(list))