#!/usr/bin/env python3
import sys

# Check the length of sys.argv
# len(sys.argv) is 1 if no arguments are provided (just the script name)
# We want exactly 3 items: [script_name, name, age]

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' name age')
    sys.exit()

# If the script gets to this point, it means the 'if' condition was False
# (meaning we HAVE exactly 3 arguments), so it's safe to continue.

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')

