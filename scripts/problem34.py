# https://projecteuler.net/problem=34

import math

# set variables
grand_total = 0

# loop through a large range
for num in range(10, 99999):
    # reset total
    total = 0
    # change number to string
    num_str = str(num)

    # loop through each number in the
    # number string
    for n in num_str:
        if total > num:
            # no need to continue with this loop
            # so break.
            break
        # total up factorials
        total += math.factorial(int(n))

    # if the factorials sum to the number
    if total == num:
        # print num and add to grand total
        print num
        grand_total += num


# print result
print 'Grand total: %s' % grand_total

