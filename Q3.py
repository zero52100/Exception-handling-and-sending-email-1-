try:
    dividend=int(input("Enter the Divindend"))
    divisor=int(input("Enter the Divisor"))
    value=dividend/divisor
    print(value)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")