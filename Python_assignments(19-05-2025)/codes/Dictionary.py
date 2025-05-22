# Can a Key Be a Value in Dictionaries?
# Yes, in Python, a dictionary’s key can be used as a value in the same dictionary or another dictionary.


# Variables for our story
name = "Harsh"
age = 22


# Dictionary : Using key, and value as key
dict1 = {
    "name": name,  # Key 'name' with value 
    "age": 32,
    name : "newHarsh", # Using the value of 'name' as a key
    "hobby": "coding"  # Just for fun
}

print(f"{dict1}") # Here we can also see that key 'age' has value '32' instead of '22' which proves dictionary is mutable

# Printing results 
print(f"{name}'s Dictionary Adventure:")
print(f"{dict1["name"]} age is {dict1['age']}, and harsh has become {dict1[name]}")