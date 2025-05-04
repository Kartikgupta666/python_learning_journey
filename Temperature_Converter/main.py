#  in this file i'm gonna make a temperature converter program with take value and the unit give the conversion temperature in C -> F or F -> C

Value= float(input("Enter the Temperature value : "))
unit = input("Enter the unit (C/F) : ").upper()

Conversion = input("Enter the value in which you want to convert it : ").upper()

match Conversion:
    case "C":
        if unit == "C":
            print(f"{Value}°C is equal to {Value}°C")
        else:
            F = (Value * 9/5) + 32
            print(f"{Value}°F is equal to {F}°C")
    case "F":
        if unit == "F":
            print(f"{Value}°F is equal to {Value}°F")
        else:
            C = (Value - 32) * 5/9
            print(f"{Value}°C is equal to {C}°F")
    case _ :
        print("Invalid conversion unit. Please enter either 'C' or 'F'.")