def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
import sys

def print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False):
    for object in objects:
        ...