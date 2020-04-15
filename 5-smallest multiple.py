"""
Smallest multiple
   
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

def gcd(n):
    for i in range(n//2, 0, -1):
        if n%i == 0:
            return i
    return n

numbers = [1, 1]
for i in range(1, 21):
    smallest_number = reduce(lambda x, y: x*y, numbers)
    if smallest_number%i != 0:
        greatest_divisor = gcd(i)
        numbers.append(i//greatest_divisor)

print(numbers)

print(reduce(lambda x, y: x*y, numbers))
