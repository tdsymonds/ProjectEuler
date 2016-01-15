# https://projecteuler.net/problem=20

import math

# set target number
num = 100
# set total to zero
total = 0

# find factorial
ans = math.factorial(num)

# convert the ans to string and then list
# so can iterate and sum
for i in list(str(ans)):
    total += int(i)

# print answer
print total
