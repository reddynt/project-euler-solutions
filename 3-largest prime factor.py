"""
Largest prime factor
   
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

number = 600851475143
# number = 13031993
primes = []

def is_prime(x):
    if x%2 == 0:
        return False
    elif any([False if x%n else True for n in range(3, int(math.sqrt(x)), 2)]):
        return False
    return True

x = 3
while (number >= 1):
    if number%x == 0 and is_prime(x):
        primes.append(x)
        number /= x
    if number == 1:
        break
    x += 2

print(primes)