class NegativeBalanceError(Exception):
    pass

class InvalidPINError(Exception):
    pass

class BankAccount:
    def __init__(self, accountno, pin, initial_balance):
        self.accountno = accountno
        self.pin = pin

        if initial_balance < 0:
            raise NegativeBalanceError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def validate_pin(self, entered_pin):
        if entered_pin != self.pin:
            raise InvalidPINError("Invalid PIN. Transaction aborted.")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        
        if self.balance - amount < 0:
            raise NegativeBalanceError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        return amount

try:
    accountno = input("Enter your bank  account number of SBM bank: ")
    pin = input("Enter your ATM PIN: ")
    initial_balance = float(input("Enter initial balance for your bank account: "))
    
    account = BankAccount(accountno, pin, initial_balance)

    entered_pin = input("Enter your ATM PIN : ")
    account.validate_pin(entered_pin)

    withdraw_amount = float(input("Enter the amount to withdraw: "))
    withdrawn = account.withdraw(withdraw_amount)
    print(f"Withdrawal successful. Updated balance: {account.balance}")

except ValueError as e:
    print(f"Error: {e}")

except InvalidPINError as e:
    print(f"Error: {e}")

except NegativeBalanceError as e:
    print(f"Error: {e}")
