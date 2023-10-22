def basisFunc():
    # Variables in python
    x = 4
    x = "sally"
    print(x)

    # Typecasting in python
    x = str(3)  # x will be '3'
    y = int(3)  # y will be 3
    z = float(3)  # z will be 3.0
    print(x, y, z)

    # Get the type of variable in python
    x = 5
    y = 10
    z = "5"
    a = 4.44
    b = 4.444444
    c = True
    print("type of x = ", type(x))
    print("type of y = ", type(y))
    print("type of z = ", type(z))
    print("type of a = ", type(a))
    print("type of b = ", type(b))
    print("type of c = ", type(c))

    # Collection unpacking in python
    fruits = ["apple", "orange", "mange", "banana"]
    w, x, y, z = fruits
    print("w: ", w)
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)

    # Data types in python
    # Numbers
    """ 
        int: 3, -8, 0
        float: 3.004, -8.7, 0.0
        complex: 6 + 2i
    """
    # Text
    """ 
        str: "Hello World"
    """
    # Boolean
    """ 
        bool: True, False
    """
    # Sequence data
    """ 
        list: [1, 2, 3, 4, 5]
    """

    # Global Variables

    def myFunc():
        # If we initialize a variable outside the function defination then it's called global variable
        # If we initialize a variable within the scope of function then it's called local variable
        local = "test"
        print("I am global variable " + x)
        print("local variable: ", local)

    myFunc()

    """ Global and local variable example """
    """ If we create a global variable and a local variable with the same name """
    print("Name conflict global varaible and local variable")
    x = "Global Variable"

    def myFunc():
        x = "Local Variable"
        print("x is ", x)

    myFunc()

    # Global Keyword

    def myFunc1():
        global testGlobal
        testGlobal = "I am a global variable.\nI am called in myFunc2.\nI am defined in myFunc1"

    myFunc1()

    def myFunc2():
        print(testGlobal)

    myFunc2()

    """ 
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType
    """
    x = "test"
    print("x is a str: ", x)
    x = 5
    print("x is a int: ", x)
    x = 5.5
    print("x is a float: ", x)
    y = 5 + 3j
    print("x is complex: ", y)
    x = ["apple", "orange", "mango", "banana"]
    print("x is a list: ", x)
    x = ("applie", "orange", "mange")
    print("x is a tuple: ", x)
    x = {"a": 1, "b": 2, "c": 3}  # holds items in key value pain
    print("x is a dict: ", type(x), x)
    x = {1, 2, 3, 3}  # all items in set are unique
    print("x is a set: ", type(x), x)

    a = 11
    print("Ternary operator example: ", True if a > 10 else False)
