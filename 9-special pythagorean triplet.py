"""
Special Pythagorean triplet
   
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
solving below equations:
c = 1000 - (a+b)**2
a**2 + b**2 = c**2

a**2 + b**2 = (1000 - (a+b)**2) = (1000**2 + (a+b)**2 - 2000a - 2000b) = (1000**2 + a**2 + b**2 + 2ab - 2000a - 2000b)
a**2 + b**2 = 1000**2 + a**2 + b**2 + 2ab - 2000a - 2000b
2ab - 2000a = 2000b - 1000**2
a(2b-2000) = 2000b - 1000**2
a = (2000b - 1000**2)/(2b-2000)
"""

import time

start = time.time()
for b in range (1, 997):
    a = int((2000*b - 1000**2)/(2*b-2000))
    c = 1000 - a - b
    if a**2 + b**2 == c**2:
        print(a*b*c)
        break
end = time.time()
print(end - start)