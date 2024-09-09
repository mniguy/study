# global variable => you can't change global variable

# if you use same name in both global and local varaible, the latter one which is the 
# local variable will only be changed and the global will remain still
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

# unboundlocalerror
def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()