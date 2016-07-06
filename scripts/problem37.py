# https://projecteuler.net/problem=37

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


# get primes
prime_list = get_prime_list(1000000)

# set initial variable for sum
grand_total = 0

# loop from primes greater than 7
for prime in prime_list[4:]:
    # assume true until proven otherwise
    truncatable_prime = True
    # save prime to string
    prime_string = str(prime)
    # truncate
    for i in range(1, len(prime_string)):
        # number not a prime
        if int(prime_string[i:]) not in prime_list or int(prime_string[:i]) not in prime_list:
            # not a trunctable prime so break
            truncatable_prime = False
            break

    if truncatable_prime:
        # add to grand total
        print prime
        grand_total += prime

# print result
print grand_total


