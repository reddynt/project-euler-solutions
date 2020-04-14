"""
Smallest multiple
   
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
from functools import reduce

def get_factors(x):
    factors = []
    if x%2 == 0:
        factors.append(2)
    for i in range(3, x, 2):
        if x%i == 0:
            factors.append(i)
    return factors


factors_set = set()
for i in range(2, 21):
    factors = get_factors(i)
    print(factors)
    factors_set = factors_set.union(set(factors))

# print(reduce(lambda x, y: x*y, all_primes))
print(factors_set)