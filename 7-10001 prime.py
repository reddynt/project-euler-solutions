"""
10001st prime
   
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import time
import math

primes_so_far = [2]
i = 3
start = time.time()
while True:  
    if all([False if i%x==0 else True for x in primes_so_far]):
        primes_so_far.append(i)
    
    if len(primes_so_far) == 10001:
        print(primes_so_far.pop())
        break
    i += 2
end = time.time()
print(end - start)