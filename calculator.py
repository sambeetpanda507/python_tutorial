def switch(operator, x, y):
    validOperators = ['+', '-', '/', '*']

    if operator not in validOperators:
        return "Invalid operator"
    elif operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    else:
        return x / y


def myCalc():
    msg1 = "Hello and welcome to calc.py"
    print(msg1)
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    msg4 = "The numbers Entered are " + str(x) + " and " + str(y)
    print(msg4)
    operator = str(input("Select the operator (+, -, /, *): "))
    result = switch(operator, x, y)
    print("Result: ", result)
