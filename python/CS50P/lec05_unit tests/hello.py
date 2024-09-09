def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    # hello(str) does not return anything but just printing str results, so testing does not work
    # print("hello,", to)
    return f"hello, {to}"

if __name__ == "__main__":
    main()