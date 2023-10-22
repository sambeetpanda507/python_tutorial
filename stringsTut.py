def myStrFunc():
    print("--- Strings in python ---")

    # Access the string char using a index
    a = "this is a string"
    index = 0
    print("char at index ", index, " is ", a[index])

    # Looping through string
    for x in "banana":
        print(x)

    # Length of string
    print("Length of a = ", len(a))

    # Check if a substring is present in a string
    txt = "Hello World"
    subStr = "sd"
    isPresent = subStr.lower() in txt.lower()
    print(isPresent)

    # Slice in string
    txt = "Hello World"
    print("Slice: ", txt[-3:])

    # Trim
    txt = "   Hello World   "
    print("Trimmed: ", txt.strip())
