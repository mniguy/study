# pypi.org/project/cowsay
# python package index
# pip

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])