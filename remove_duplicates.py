"""
Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Write two different functions to do this - 
one using a loop and constructing a list, and another using sets.

"""

" List "
listNum = [1,2,3,1,1,6,4,3,4,5,]

def removeDuplicates(listNum):

    newList = []
    
    for x in listNum:
        if x not in newList:
            newList.append(x)

    print(newList)

removeDuplicates(listNum)

" Sets "

def delDuplicates(listNum):

    setNum = set()
    setNums = set(listNum)
    setNums = list(setNums)
    print(list(setNums))        


delDuplicates(listNum)