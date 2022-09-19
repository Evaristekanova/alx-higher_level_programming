#!usr/bin/python3
"""
module:print_square
"""
def print_square(size):
    """
    printing square of # sabed on the size passed
    """
    if type(size) is not int:
        raise TypeError("size must be integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
