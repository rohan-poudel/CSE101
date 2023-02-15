# CSE 101, Assignment 1, Problem 4


def fillPool(length, width, height, gpm):
    vol = length * width * height
    vol = vol * 264.172
    time = vol / gpm
    return time


# Test cases below. Note this is one method of making a formatted string
print(f'{fillPool(10, 10, 10, 1000):0.3f}')
print(f'{fillPool(12, 13, 20, 3000):0.3f}')
print(f'{fillPool(10, 40, 8, 250):0.3f}')