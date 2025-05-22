"""
Data Types are defined as the type of the data a variable holds.
For Example :- int, float, string, boolean, list, tuple, dictionary, set, noneType.
"""

# Example code :)
a = 1 # a is an integer 
b = 3.14 # b is a floating point numbers
c = "Harsh" # c is a string
d = True # d is a boolean type variable 
e = None # e is a none type variable
list1 = [1, "apple", 3.14] # list type variable
tuple1 = (5, 20, 3) # tuple type variable
dict1 = {"name": "harsh", "Age" : 22} # dictionary type variable
set1 = {3, 8, 10} # set type variable

# Some alterations
add = a+b
append1 = list1.append("Banana")
set1.add(22)

# Final print statement
print(f"""{c} adds {a} and {b} to get {a + b}, and the result is {add == add} which is {d}. 
      \nAlso {c} wants to add a banana to list1 to make it {list1}.
      \nAlso {c} wants to access tuple item 2 which is {tuple1[1]}.
      \nAnd access name value in dictionary that is {dict1["name"]}.
      \nlastly wants to add 22 in set1 to get {set1}""")


