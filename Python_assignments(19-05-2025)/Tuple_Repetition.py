# tuple*n repetation what does it do?
'''This is called tuple repetition.
The * operator duplicates the entire tuple n times and concatenates the copies into a single new tuple. 
For example, ("a", "b") * 2 results in ("a", "b", "a", "b").
'''

# Example Code :)
# Tuple * n repeats the tuple n times to create a new tuple!

name = "Harsh"
age = 22

# Tuple: Harsh's favorite activities
activity_tuple = ("coding", "gaming")

# 1. Repeat tuple 3 times
repeated_tuple = activity_tuple * 3

# 2. Repeat tuple 1 time (no change)
single_repeat = activity_tuple * 1

# 3. Repeat tuple 0 times (empty tuple)
empty_repeat = activity_tuple * 0

# 4. Repeat a single-item tuple
single_item_tuple = (age,)  # Note the comma for single-item tuple
repeated_age = single_item_tuple * 4

# Printing results with f-strings
print(f"{name}'s Tuple Multiplier Adventure:")
print(f"Original tuple: {activity_tuple}")
print(f"Repeating {activity_tuple} 3 times: {repeated_tuple}")
print(f"Repeating {activity_tuple} 1 time: {single_repeat}")
print(f"Repeating {activity_tuple} 0 times: {empty_repeat}")
print(f"Single-item tuple {(age,)} repeated 4 times: {repeated_age}")
print(f"{name} sees the original tuple is unchanged: {activity_tuple}")
