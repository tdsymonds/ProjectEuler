# https://projecteuler.net/problem=53

import math

def ncr(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

# set the initial variables
limit_for_n = 100
number_greater_than_one_million = 0

# loop through each possible value of n
for n in range(0,limit_for_n+1):
    # loop through each possible value of r
    for r in range(0, n+1):
        # if ncr is greater than one million
        if ncr(n,r) > 1000000:
            # increase counter
            number_greater_than_one_million += 1

# print result
print number_greater_than_one_million