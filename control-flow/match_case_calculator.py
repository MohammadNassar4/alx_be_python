num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operations = input("Choose the operation (+, -, *, /): ")

match operations:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num1 == 0 or num2 == 0:
            print("Can't devide by Zero.")
        else:
            print(num1 / num2)