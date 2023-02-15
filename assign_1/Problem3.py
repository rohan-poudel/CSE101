# CSE 101, Assignment 1, Problem 3


# Below are the definitions for 4 different functions.

def hello():
    print('Hello world!')

def square(n):
    return n * n


def add(x, y):
    return x + y


def printSum(x, y):
    print(x + y)

def name():
    print('"Rohan Poudel"')
    print('\t Computer Science 2021')


# Below you are testing the functions that you defined above.
# Call each function as many times as you see necessary.
#
# In testing a function you should call print function with the function
# call if the function is a fruitful function like 'square' and 'add' above.
# If you are calling a void function like 'hello' and 'printSum' above,
# don't call print with the function call.

# Testing hello
print('Testing hello:')
print('hello(): ', end='')
hello() # This is a test case, which tests the function and prints the result
print()

# Testing square
print('Testing square:')
print('square(2) = ' + str(square(2))) # This is a test case, which tests the function with specific input and prints the result
print('square(4) = ' + str(square(4))) # This is a test case, which tests the function with specific input and prints the result
print()

# Testing add
print('Testing add:')
print('add(3, 5) = ' + str(add(3, 5))) # This is a test case, which tests the function with specific input and prints the result
print('add(23, 58) = ' + str(add(23, 58))) # This is a test case, which tests the function with specific input and prints the result
print()

# Testing printSum
print('Testing printSum:')
print('printSum(4, 21) = ', end='')
printSum(4, 21) # This is a test case, which tests the function with specific input and prints the result

#testing name
print('Testing name:')
name()
