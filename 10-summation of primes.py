"""
Summation of primes
   
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def is_prime(x):
    if x%2 == 0 and x!=2:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x%i == 0:
            return False
    return True

sum_of_primes = 2

for i in range(3, 2000000):
    if is_prime(i):
        print(i)
        sum_of_primes += i

print(sum_of_primes)