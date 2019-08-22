def swap(l,i,j):
    l[i], l[j] = l[j], l[i]

def insertionSort(mylist):
    size = len(mylist)
    for passnum in range(1, size):
        current = mylist[passnum]
        index = passnum
        while (index > 0 and current < mylist[index-1]):
            mylist[index] = mylist[index-1]
            index -=1
        mylist[index] = current
def main():
    l = [54,26,93,17,77,31,44,55,70]
    insertionSort(l)
    print(l)

if __name__ == "__main__": 
    main()
