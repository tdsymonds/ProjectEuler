# https://projecteuler.net/problem=21

import math

def proper_divisor_sum(n):
    limit = int(math.ceil(n/2.0))
    proper_divisors = []

    for i in range(1,limit+1):
        if n % i == 0:
            proper_divisors.append(i)

    return sum(proper_divisors)


# set initial variables
grand_sum = 0

# loop through numbers up to 10,000
for i in range(1, 10000):
    # calculate d(a) and d(b)
    a = i
    b = proper_divisor_sum(a)
    c = proper_divisor_sum(b)
    
    # if d(a) = b and d(b) = a
    # where a ≠ b
    if a == c and a != b:
        # add to sum
        grand_sum += a + b

# print result halfed, as pairs of numbers 
# are counted twice, e.g. 220 + 284 and 
# 284 + 220
print grand_sum / 2

