#https://projecteuler.net/problem=12

import time

start = time.time()


max_divisors_found = 0
max_divisors = 500

i = 1

while (max_divisors_found < max_divisors):

    # calc triangle number
    triangle_number = sum(range(1, i + 1))
    
    # reset variables
    factors = []
    num = 1

    # iterate through numbers to find factors
    while (num <= triangle_number):
        # we're halfway through the list of factors and
        # so the list repeats from here, so stop.
        if num in factors:
            break

        if triangle_number % num == 0:
            # the number is a factor
            factors.append(num)
            # the quotient is a factor
            factors.append(triangle_number / num)

        # increment
        num += 1

    # assign number of divisors to variable
    max_divisors_found = len(factors)

    i += 1

print triangle_number


end = time.time()
print 'Run time: %s seconds' % (end - start)

