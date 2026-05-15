#!/usr/bin/env python3
import sys

# Assign arguments from the command line to objects
# sys.argv[0] is the script name itself
# sys.argv[1] is the first item after the script name
# sys.argv[2] is the second item after the script name

name = sys.argv[1]
age = int(sys.argv[2]) # Although the requirement says integer object, arguments are read as strings

print('Hi ' + name + ', you are ' + str(age) + ' years old.')
