class InvalidAgeError(Exception):
    pass
try:
    age=int(input("Enter the your age"))
    if age <0 or age>150:
        raise InvalidAgeError
    print(f"Your age is {age}")
except InvalidAgeError:
     print("Invalid age entered. please enter age between 1 and 150")
except ValueError:
    print("Error: Please enter a valid integer for age.")