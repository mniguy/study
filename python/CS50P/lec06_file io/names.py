# 01
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")

# 02
name = input("What's your name? ")

# "a" : append
# "w" : write
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# 03
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line)    

# 04
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# 05
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
# sorted(iterable, /, *, key=None, reverse=False)
for name in sorted(names, reverse=True):
    print(f"hello, {name}")

# 06
with open("names.txt") as file:
    for line in sorted (file):
        print("hello,", line.rstrip())
