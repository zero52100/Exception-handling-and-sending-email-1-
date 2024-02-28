try:
    user_input=int(input("Enter your favorite  int number :"))
    print(f"Your favorite int number {user_input}")
except ValueError:
    print("Invalid input")