def calculator():
    print("Welcome to the Calculator!")

    while True:
        try:
            num1 = float(input("Enter the initial number"))
        except ValueError:
            print("Invalid Input")

        try:
            num2 = float(input("Enter the next number"))
        except ValueError:
            print("Invalid Input")

        Operator = input("Enter an arithmitic operator: + - / * ")
        try:
            if Operator == "+":
                result = num1 + num2
            elif Operator == "-":
                result = num1 - num2
            elif Operator == "*":
                result = num1 * num2
            elif Operator == "/":
                result = num1 / num2 
            else:
                raise ValueError("Invalid Operator")
        except ValueError:
            print("Invalid Operator please use one of these: +, -, /, *")

        print(f"The result is: {result}")

        finishcalc = input("Would you like to continue? yes/no").strip().lower()
        if finishcalc == "no":
            print("Thanks for using the calculator!")
            break

calculator()





