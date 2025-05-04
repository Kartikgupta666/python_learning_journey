#  this is the calculator 
# this calculator performs operation using two number

sign = input('Enter the operation options are \n + \n - \n * \n / \n ** \n % \n You choose : ')
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

match sign:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    case _:
        print("Invalid operation")
        