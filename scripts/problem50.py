# https://projecteuler.net/problem=50

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
    Returns true if prime. Divides number by all primes in
    the list up to the square root of the number.
    """
    sqrt = math.sqrt(number)
    i = 0
    prime = prime_list[i]
    while prime <= sqrt:
        if number % prime == 0:
            return False
        i += 1
        prime = prime_list[i]
    return True


# first get a big list of primes
full_prime_list = get_prime_list(100000)

# set max number
max_number = 1000000

# reset variables
max_length = 0
max_prime = 0

# loop through each prime to start the consecutive primes list from
for index, starting_prime in enumerate(full_prime_list):
    # initialise prime list
    prime_list = [starting_prime]
    # loop through each consecutive prime
    for prime in full_prime_list[index+1:]:
        # add the prime to the list
        prime_list.append(prime)
        # calculate the sum and length
        prime_list_sum = sum(prime_list)
        prime_list_length = len(prime_list)
        
        # if the sum is greater than the max then
        # no point continuing
        if prime_list_sum >= max_number:
            break

        # if the sum is prime and greater then the max length
        if prime_list_length > 1 and is_prime(prime_list_sum, full_prime_list) and prime_list_length > max_length:
            # update max length and the max prime found
            max_length = prime_list_length
            max_prime = prime_list_sum


# print result
print max_prime