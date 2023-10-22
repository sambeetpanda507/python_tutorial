def myFunc():
    myList = [1, 2, 3, 4]

    # Push: Add to the end of list
    myList.append(5)
    myList.append(3)
    print(myList)

    # Insert at specific index
    myList.insert(2, 44)
    print(myList)

    # Pop: Removes from specified index and if not index present then remove the last element
    myList.pop()
    print(myList)

    # Filter
    myList.remove(3)
    print(myList)

    # findIndex
    index = myList.index(5)
    print(index)

    # concat
    list1 = ['a', 'b', 'c']
    list2 = ['d', 'e', 'f']
    for c in list2:
        list1.append(c)

    print("Concat: ", list1)
