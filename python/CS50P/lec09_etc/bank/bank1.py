class Account:
    def __init__(self) -> None:
        # effectively indicate that it is a private variable
        self._balance = 0

    @property
    def balance(self) -> None:
        return self._balance
    
    def deposit(self, n=int) -> None:
        self._balance += n
    
    def withdraw(self, n=int) -> None:
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()