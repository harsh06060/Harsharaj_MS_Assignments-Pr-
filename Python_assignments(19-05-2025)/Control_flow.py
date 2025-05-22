'''
Control Flow in Python manages how a program executes code based on conditions and repetition:

While Loop: Repeats a block of code as long as a condition is True. 
It’s great for scenarios where you don’t know how many iterations you need upfront (e.g., keep asking for input until valid).
Match-Case (Switch-Case Equivalent): 
Introduced in Python 3.10, the match statement evaluates a variable against multiple patterns and executes the corresponding block. It’s like a cleaner, more powerful version of multiple if-elif statements.
'''

# Control Flow: Harsh's Calculator Menu Adventure
# While loop keeps the menu running, match-case handles user choices!


name = "Harsh"
num1 = 10
num2 = 5

# While loop: Run until Harsh chooses to exit
running = True
print(f"{name}'s Calculator Menu Adventure Begins!")
print(f"Numbers: {num1} and {num2}")

while running:
    # Get user choice
    choice = input(f"\n{name}, pick an option (add, subtract, multiply, exit): ").lower()

    # Match-case to handle choices
    match choice:
        case "add":
            result = num1 + num2
            print(f"{name} adds {num1} + {num2} = {result}")
        case "subtract":
            result = num1 - num2
            print(f"{name} subtracts {num1} - {num2} = {result}")
        case "multiply":
            result = num1 * num2
            print(f"{name} multiplies {num1} * {num2} = {result}")
        case "exit":
            print(f"{name} says goodbye to the calculator!")
            running = False  # Exit the loop
        case _:
            print(f"Oops, {name}! That's not a valid option. Try again.")

print(f"{name}'s adventure ends. Come back soon!")