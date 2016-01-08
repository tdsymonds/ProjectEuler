# https://projecteuler.net/problem=9

import math

triplet_sum = 1000
found = False

# knowing a < b < c we can find
# max value for a
max_a = (triplet_sum // 3) - 1

# loop through poss values of a
for a in range(1, max_a + 1):
    # loop through possible values for b
    for b in range(a + 1, triplet_sum):
        # calculate c
        c_squared = (a ** 2) + (b ** 2)
        c = math.sqrt(c_squared)

        if a + b + c == triplet_sum:
            # sums to triplet_sum, so found
            found = True
            break
        
    if found:
        break

if found:
    print a * b * c
