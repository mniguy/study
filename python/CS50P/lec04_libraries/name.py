# command-line arguements
# docs.python.org/3/library/sys.html
# sys.argv

# sys.argv[0] == name of the problem
# sys.argv[1] == 내가 지정한 이름
# print("hello, my name is", sys.argv[1]) 

import sys

if len(sys.argv) < 2:
    sys.exit("Too few argeuments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])


import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)