# https://projecteuler.net/problem=46

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
prime_list = get_prime_list(100000)

for number in range(3, 10000, 2):
    # not composite so skip
    if number in prime_list:
        continue
    
    # set initial variables
    can_be_written = False
    i = 1
    twice_a_square = 2*i**2

    # loop up to within 2 (smallest prime) 
    # of the number
    while twice_a_square < number-2:
        # if difference is prime
        if (number - twice_a_square) in prime_list:
            # can be written so break
            can_be_written = True
            break
        # increment and recalculate square
        i += 1
        twice_a_square = 2*i**2
    
    # if it can't be written
    if not can_be_written:
        # break and print result
        print number
        break
