def calculator():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if (operator == '+'):
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            return
    else:
        print("Invalid operator.")
        return

    print("Result: ", result)


calculator()
