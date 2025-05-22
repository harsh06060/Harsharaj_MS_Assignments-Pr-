# Operators
# Operators are symbols that perform operations on variables and values.

"""
Python has several types of operators :
1) Arithmetic Operators: For mathematical calculations.
2) Comparison Operators: To compare values.
3) Logical Operators: To combine conditions.
4) Assignment Operators: To assign values to variables.
5) Membership Operators: To check if a value is in a sequence.
6) Identity Operators: To check if objects are the same.
"""

# Variables for examples
a = 10
b = 3
name = "Harsh"
list1 = [1, 2, 3, 4]
list2 = list1  # Same object for identity operator

# 1. Arithmetic Operators
add = a + b  # Addition
subtract = a - b  # Subtraction
multiply = a * b  # Multiplication
divide = a / b  # Division
floor_div = a // b  # Floor Division
modulo = a % b  # reminder
power = a ** 2  # Exponentiation

# 2. Comparison Operators
equal = a == b  # Equal to
not_equal = a != b  # Not equal to
greater = a > b  # Greater than
less = a < b  # Less than
greater_equal = a >= b  # Greater than or equal to
less_equal = a <= b  # Less than or equal to

# 3. Logical Operators
condition1 = True
condition2 = False
logical_and = condition1 and condition2  # Logical AND
logical_or = condition1 or condition2  # Logical OR
logical_not = not condition1  # Logical NOT

# 4. Assignment Operators
x = 5  # Simple Assignment
x += 2  # Add and assign
y = 10 # Simple Assignment
y *= 3  # Multiply and assign

# 5. Membership Operators
in_list = 3 in list1  # Check if 3 is in list1
not_in_list = 5 not in list1  # Check if 5 is not in list1

# 6. Identity Operators
is_same = list1 is list2  # Check if list1 and list2 are the same object
is_not_same = list1 is not [1, 2, 3, 4]  # Check if list1 is not a new list

# Printing results 
print(f"{name}'s Operator Demo:")
print(f"Arithmetic: {a} + {b} = {add}, {a} - {b} = {subtract}, {a} * {b} = {multiply}")
print(f"More Arithmetic: {a} / {b} = {divide}, {a} // {b} = {floor_div}, {a} % {b} = {modulo}, {a} ** 2 = {power}")
print(f"Comparison: {a} == {b} is {equal}, {a} != {b} is {not_equal}, {a} > {b} is {greater}")
print(f"More Comparison: {a} < {b} is {less}, {a} >= {b} is {greater_equal}, {a} <= {b} is {less_equal}")
print(f"Logical: {condition1} AND {condition2} = {logical_and}, {condition1} OR {condition2} = {logical_or}, NOT {condition1} = {logical_not}")
print(f"Assignment: x = 5, then x += 2 gives x = {x}, y = 10, then y *= 3 gives y = {y}")
print(f"Membership: Is 3 in {list1}? {in_list}, Is 5 not in {list1}? {not_in_list}")
print(f"Identity: Is list1 same as list2? {is_same}, Is list1 not a new [1, 2, 3, 4]? {is_not_same}")