#https://projecteuler.net/problem=5

not_found = True
num = 0

while (not_found):
    
    not_found = False
    
    # to increase efficiancy, rather than try
	# every number, can increase in steps 
	# of 19 * 20.
    num += 20 * 19

    for i in range(1,20):
        
        if num % i != 0:
        	# number does not evenly divide
        	# one of the numbers, so break
        	# loop to skip to next num
            not_found = True
            break
    
print num