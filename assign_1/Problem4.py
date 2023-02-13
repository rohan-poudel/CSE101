# CSE 101, Assignment 1, Problem 4


def fillPool(length, width, height, gpm):
    length = length
    width = width
    height = height
    gpm = gpm
    vol = length * width * height
    vol = float(vol) * 264.172
    time = vol / gpm
    return print(f"The time need is {time:0.3f} minutes")


# Test cases below. Note this is one method of making a formatted string
fillPool(10, 10, 10, 1000)
fillPool(12, 13, 20, 3000)
fillPool(10, 40, 8, 250)