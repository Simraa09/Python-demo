print("CALCULATOR")
while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Division\n5. Factorial\n6. Exit\n")
    i = int(input("Enter the operation: "))

    match i:
        case 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a + b)

        case 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a - b)

        case 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a * b)

        case 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)

        case 5:
            a = int(input("Enter a number: "))
            fact = 1
            n = a
            while n > 0:
                fact = fact * n
                n -= 1
            print("Result =", fact)

        case 6:
            print("Program Exited")
            break

        case _:
            print("Invalid choice")