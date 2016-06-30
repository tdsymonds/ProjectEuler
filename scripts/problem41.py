# https://projecteuler.net/problem=41

import itertools
import math


def get_prime_list(n):
    """ 
    Returns  a list of primes < n 
    
    Function taken from:
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
    """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def is_prime(number, prime_list):
    """
    Checks number against all primes in
    list. If a prime, returns True
    """
    for prime in prime_list:
        if number % prime == 0:
            return False
    return True


# the largest possible pandigital is:
largest_pandigital = 987654321

# therefore the largest prime we need to check up
# to is the sqrt of the largest number.
# this is rounded up.
largest_prime_to_check = math.sqrt(largest_pandigital)
largest_prime_to_check = math.ceil(largest_prime_to_check)

# get all primes up to this number
prime_list = get_prime_list(int(largest_prime_to_check))

# set iterator and variable
not_found = True
i = 9

# loop until found or hits 1
while not_found or i < 2:
    
    # create a list of all pandigitals up to length i
    lst = range(1, i)
    all_lists = list(itertools.permutations(lst))
    all_numbers = []
    for lst in all_lists:
        all_numbers.append(int(''.join(map(str, lst))))

    # reverse sort the list, so largest is first.
    all_numbers.sort(reverse=True)

    # loop through each pandigital and check
    # if prime
    for number in all_numbers:
        if is_prime(number, prime_list):
            # prime found so print and stop looking.
            print 'Number: %s' % (number)
            not_found = False
            break

    # decrement i
    i -= 1
