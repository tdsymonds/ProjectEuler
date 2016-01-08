#https://projecteuler.net/problem=15

import math
import time
start = time.time()

# the start is 0, 0
# set co-ordinates of path end
x = 20
y = 20

# set parameters for binomial coefficient
n = x + y
k = y

# calculate binomial coefficient and print result
print (math.factorial(n)) / (math.factorial(k) * math.factorial(n - k))

end = time.time()
print 'Run time: %s seconds' % (end - start)
