#!/usr/bin/env python3

# Prompting the user for data
name = input("Name: ")
age = input("Age: ")

# Displaying the final output
# Note: we use str(age) just in case, though input() defaults to string
print('Hi ' + name + ', you are ' + str(age) + ' years old.')
