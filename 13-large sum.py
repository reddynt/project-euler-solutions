"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import os

def read_input():
    with open('./input/13.txt', 'r') as input_file:
        input_file = input_file.read()
        input_numbers = [int(x) for x in input_file.split()]
    print(sum(input_numbers))

read_input()