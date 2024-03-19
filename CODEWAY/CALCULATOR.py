def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter operation choice (1/2/3/4): ")

    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation choice.")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")

calculator()

