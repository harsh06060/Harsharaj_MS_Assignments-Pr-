"""
-> Floor division is a mathematical operation in Python that divides two numbers 
and rounds the result down to the nearest integer.
-> It is performed using the // operator. Unlike regular division (/), 
which returns a floating point number.
-> Thus Floor divion always returns an integer value and not a floading point value.
"""

# Here are some simple examples :)
# Regular Divison 1
num1 = 7.5
num2 = 2
regular_division = num1/num2

# f strings are the best , i use thema lot :)
print(f"Regular division of 7.5/2 : {regular_division}") # Returns decimal value


# Regular Divison 2
num3 = -7.5
num4 = 2
regular_division1 = num3/num4
print(f"Regular division of -7.5/2 : {regular_division1}") # Returns decimal value


# Floor Division 1
n1 = 7.5
n2 = 2
floor_division = n1//n2
print(f"Floor Divison of 7.5//2 : {floor_division}") # Returns lower integer value


# Floor Division 2
n3 = -7.5
n4 = 2
floor_division1 = n3//n4
print(f"Floor Divison of -7.5//2 : {floor_division1}") # Returns lower integer value