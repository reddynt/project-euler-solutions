"""
Largest palindrome product
   
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# brute force
from itertools import combinations

all = list(combinations(range(999, 100, -1), 2))

def is_palindrome(n):
    if len(n) == 0 or len(n) == 1:
        return True
    if n[-1] == n[0]:
        return is_palindrome(n[1:-1])
    return False

# print(is_palindrome('12344321'))

palindromes = []
for a, b in all:
    if is_palindrome(str(a * b)):
        palindromes.append((a, b, a * b))

palindromes = sorted(palindromes, key=lambda x: x[2], reverse=True)
print(palindromes[:10])
