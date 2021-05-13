"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

def num_routes(n):
    return math.factorial(2*n)/(math.pow(math.factorial(n), 2))

print(num_routes(20))