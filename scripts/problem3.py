#https://projecteuler.net/problem=3

#Method:
#To find prime factors, first evenly divide (no remainder) by two and the subsequent 
#resulting quotients as many times as possible. Every time it divides add a two to the list.
#Once no more even divisons can be made increase two by one, so three and repeat.
#Repeat process until the resutling quotient remaining = 1.

number_to_factor = 600851475143
prime_factor_list = []
num = 2

while (number_to_factor != 1):
    if number_to_factor % num == 0:
    	# even division, so save quotient
    	# for next iteration
        number_to_factor /= num
        # add num to the prime factor list
        prime_factor_list.append(num)
    else:
    	# not even division, try for next
    	# value of num
        num += 1

print max(prime_factor_list)


