# https://projecteuler.net/problem=10

# Solution uses the Sieve of Eratosthenes. More info found here:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math

max_prime_size = 2000000

# starting position in list
pos = 0
# starting value for while loop
p = 2

# create list of numbers
num_list = range(1, max_prime_size + 1)

# need to loop for all values up to sqrt of max prime size
while (p <= int(math.sqrt(max_prime_size))):

    # increment
    pos += 1
    i = 2
    # get next value in list
    p = num_list[pos]

    # if marked move on to next
    if not p:
        continue

    # mark the multiples of p by setting as none
    while (i * p <= max_prime_size):
        num_list[(i * p)-1] = None
        i += 1


# Remove marked numbers and delete 1 from list 
num_list = [x for x in num_list if x is not None]
del num_list[0]


print sum(num_list)

