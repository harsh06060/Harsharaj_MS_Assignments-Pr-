'''
Both lists and tuples are used to store collections of items in Python, but they have key differences:

Mutability:
List: Mutable, meaning you can change its contents (add, remove, or modify items) after creation.
Tuple: Immutable, meaning once created, you cannot change its contents (no adding, removing, or modifying items).

Syntax:
List: Defined using square brackets, e.g., [1, 2, 3].
Tuple: Defined using parentheses, e.g., (1, 2, 3).

Performance:
List: Slightly slower because it’s mutable and needs to handle changes.
Tuple: Faster because it’s immutable, making it more memory-efficient and optimized for fixed data.

Use Cases:
List: Use when you need a collection that might change, like a shopping list or a list of tasks.
Tuple: Use for fixed data that shouldn’t change, like coordinates, days of the week, or constant values.
'''

# Also, tuple.clear() is not possible in python as tuples are immutable

# Example code :)
# Tuples vs Lists: Harsh's Collection Adventure
# Lists are mutable and use [ ], Tuples are immutable and use ( )

# Variables for our story
name = "Harsh"
age = 22

# List: Harsh's favorite hobbies (mutable)
hobby_list = ["coding", "gaming", "reading"]

# Tuple: Harsh's fixed profile info (immutable)
tuple = (name, age, "student")

# Operations on List (mutable)
hobby_list.append("painting")  # Add a new hobby
hobby_list[1] = "swimming"    # Change 'gaming' to 'swimming'

# Operations on Tuple (immutable, so we can't change it)
# tuple[1] = 23  # This would cause an error!
tuple_access = tuple[1]  # Access age (22)
tuple_length = len(tuple) # number of items in the tuple
tuple_count = tuple.count('student') # Count occurances of an item in the tuple

try:
    tuple.clear()  # This will raise an error
except AttributeError:
    error_message = f"Oops! {name} can't clear a tuple because it's immutable!"

# Printing results with f-strings
print(f"{name}'s Collection Adventure:")
print(f"Original hobby list(can't get the original as it's mutable and items have been edited): {hobby_list}")
print(f"After adding 'painting' and changing 'gaming' to 'swimming': {hobby_list}")
print(f"{name}'s profile tuple: {tuple}")
print(f"Accessing tuple age: {tuple_access}")
print(f"Accessing tuple length: {tuple_length}")
print(f"Accessing tuple count for name: {tuple_count}")
print(f"Tryping to Clear a tuple! : {error_message}")