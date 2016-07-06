# https://projecteuler.net/problem=35

# Sadly takes 11 minutes to run, which breaks the 1 minute golden
# rule. Struggling to find a more efficient solution :(


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


def get_rotations(number):
    # set initial variables
    rotations = []
    original_number_string = number_string = str(number)
    # loop forever whilst rotating digits
    while True:
        # add rotation to list
        rotations.append(int(number_string))
        # rotate
        digit_list = list(number_string)
        digit_list.append(digit_list.pop(0))
        number_string = ''.join(digit_list)
        
        # if we're back to the starting number then break
        if number_string == original_number_string:
            break

    return rotations


# get primes up to a million
prime_list = get_prime_list(1000005)

# set intial variables
i = 0
prime = prime_list[0]
circular_prime_list = []
non_circular_prime_list = []

# while the prime is under a million loop
while prime < 10 ** 6:
    # if rotation of prime already processed
    if prime in circular_prime_list or prime in non_circular_prime_list:
        # increment and continue
        i += 1
        prime = prime_list[i]
        continue

    # get rotations
    rotations = get_rotations(str(prime))
    # assume circular prime until proven otherwise
    circular_prime = True
    # loop through each rotation
    for rotation in rotations:
        # if the number is not prime
        if rotation not in prime_list:
            # not a circular prime
            circular_prime = False
            non_circular_prime_list += rotations
            break

    # number is a circular prime
    if circular_prime:
        # add rotations to list
        circular_prime_list += rotations

    # increment and get next prime
    i += 1
    prime = prime_list[i]


# print result
print len(circular_prime_list)