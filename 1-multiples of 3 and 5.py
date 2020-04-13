"""

Multiples of 3 and 5
   
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

# i = 0
# total = 0
# while (i < 1000):
#     if i%3 == 0 or i%5 == 0:
#         total += i
#     i += 1

# print(total)

def ap_sum(number, threshold):
    """ arithmetic progression sum """
    a = number
    d = number
    n = (threshold - 1) // a
    return (n / 2) * (2 * a + (n - 1) * d)

print(ap_sum(3, 1000) + ap_sum(5, 1000) - ap_sum(15, 1000))