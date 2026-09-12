a= float(input("Enter first number: "))
b= float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")

match choice:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case "/":
        if b == 0:
            print("cannot divide by zero")
        else:
            print("Result =", a / b)
    case _:
        print("Invalid choice")