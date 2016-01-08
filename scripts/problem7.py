#https://projecteuler.net/problem=7

import math

#starting prime list
prime_list = [2,3,5,7,11,13]
#the next num after the end of the prime list
num = prime_list[-1] + 1

#whilst prime_list length is less than target
while len(prime_list) < 10001:

    #the number is a prime unless we find a factor
    prime = True

    #Only need to check factors up to the sqrt of the num
    max_prime_check = int(math.sqrt(num))

    #loop through each prime in the list
    for existing_prime in prime_list:

        if existing_prime > max_prime_check:
            #bigger than sqrt so no need to continue checking
            #break the loop
            break
        
        if num % existing_prime == 0:
            #has a factor so not a prime.
            #break the loop
            prime = False
            break

    #We've checked primes, so if no factor found then
    #number is prime and add to the list.
    if prime:
        prime_list.append(num)

    #Check the next num
    num += 1


#print the target prime
print prime_list[-1]
