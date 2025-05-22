'''
Is Class an Object? 
Yes! In Python, a class is an object!
'''

# Example code :)

name = "Harsh"

class Quest:
    pass  

harsh_quest = Quest() # an instance

class_type = type(Quest)
instance_type = type(harsh_quest)

print(f"{name}'s Simple OOP Quest:")
print(f"Quest class is a {class_type}")
print(f"Harsh's quest instance is a {instance_type}")
