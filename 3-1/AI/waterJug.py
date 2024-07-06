# Initial quantities in the jugs
x = 0
y = 0
# Input the sizes of the jugs
jug1_capacity = int(input("Enter the size of jug1: "))
jug2_capacity = int(input("Enter the size of jug2: "))
# The goal is to have exactly 2 units in jug1
goal = 2
while x != goal:
    # Display current state
    print(f"Current state: Jug1 = {x}, Jug2 = {y}")
    # Input the rule number
    rule = int(input("\nEnter the rule number: "))
    if rule == 1:
        # Fill jug1
        x = jug1_capacity
        print(f"Action: Fill Jug1 -> Jug1 = {x}, Jug2 = {y}")
    elif rule == 2:
        # Fill jug2
        y = jug2_capacity
        print(f"Action: Fill Jug2 -> Jug1 = {x}, Jug2 = {y}")
    elif rule == 3:
        # Pour water from jug1 to jug2 until jug2 is full or jug1 is empty
        transfer = min(x, jug2_capacity - y)
        x -= transfer
        y += transfer
        print(f"Action: Pour from Jug1 to Jug2 -> Jug1 = {x}, Jug2 = {y}")
    elif rule == 4:
        # Pour water from jug2 to jug1 until jug1 is full or jug2 is empty
        transfer = min(y, jug1_capacity - x)
        y -= transfer
        x += transfer
        print(f"Action: Pour from Jug2 to Jug1 -> Jug1 = {x}, Jug2 = {y}")
    elif rule == 5:
        # Empty jug1
        x = 0
        print(f"Action: Empty Jug1 -> Jug1 = {x}, Jug2 = {y}")
    elif rule == 6:
        # Empty jug2
        y = 0
        print(f"Action: Empty Jug2 -> Jug1 = {x}, Jug2 = {y}")
    else:
        print("Invalid rule number. Please enter a number between 1 and 6.")
print(f"Goal achieved: Jug1 = {x}, Jug2 = {y}")
