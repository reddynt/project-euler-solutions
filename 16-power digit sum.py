"""
power(2, 15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number power(2, 1000)?
"""

import math

def get_sum(n):
    power_value = 2**n
    answer = 0

    while True:
        if power_value == 0:
            break
        answer += power_value%10
        power_value = power_value//10
    return answer

answer = get_sum(1000)
print(answer)

print(sum(map(int, str(2**1000))))