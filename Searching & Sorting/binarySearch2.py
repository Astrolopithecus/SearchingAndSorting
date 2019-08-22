#Program to search through a sorted list using a binary search algorithm
#Iterative version returns the index of the item if found, otherwise returns -1
def binarySearch(value, mylist):
    low = 0
    high = len(mylist)-1

    while (low <= high):
        mid = (low + high) // 2
        if (mylist[mid] == value):
            #Found it
            return mid
        if (mylist[mid] < value):
            #Search in upper half
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Recursive version returns the index of the item if found, otherwise returns -1
##def binarySearchRecursive(mylist, value):
##    if len(mylist) = 0:
##        return -1 #Base case
##    else:
##        #Check midpoint
##        mid = len(mylist) // 2
##        if (mylist[mid] == value):
##            #Found it
##            return mid
##        else: #Figure out which half to explore next
##            if (mylist[mid] < value):
##                #Search in upper half
##                return binarySearchRecursive(mylist[mid + 1:], value)
##            else:
##                #Search in lower half
##                return binarySearchRecursive(mylist[:mid], value)
