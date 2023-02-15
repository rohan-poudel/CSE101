# CSE 101, Assignment 2, Problem 1
#BUG1 is inline 16 the print statement runs everytime the function is called so we need to use elif statement.
#BUG2 is in line 16 there is mistake using single quotations
#BUG3 is in line 13 it was missing one more "=". 

def shapeName(numberOfSides):
    if numberOfSides == 3:
        print('triangle')
    elif numberOfSides == 4:
        print('square')
    elif numberOfSides == 5:
        print('pentagon')
    elif numberOfSides == 6:
        print('hexagon')
    elif numberOfSides > 6:
        print("Can't tell what shape this is, too many sides!")

# Below are 3 example test cases
print("Testing shapeName(3): ", end="")
shapeName(3)
print()

print("Testing shapeName(4): ", end="")
shapeName(4)
print()

print("Testing shapeName(5): ", end="")
shapeName(5)
print()

print("Testing shapeName(10): ", end="")
shapeName(10)