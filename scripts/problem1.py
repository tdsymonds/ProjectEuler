#https://projecteuler.net/problem=1

the_sum = 0

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
    	# multiple of 3 or 5
    	# so sum
        the_sum += i

print the_sum
