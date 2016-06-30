# https://projecteuler.net/problem=40

# concatenate the numbers with plenty of 
# cushion
long_num = ''
for num in range(1, 1000000):
    long_num += str(num)

# set product variable
product = 1

# loop through each of the powers
# to get the relevant digits and
# mutlipy the product by this
for i in range(1, 8):
    d = 10 ** (i - 1) 
    product *= int(long_num[d-1])

# print result
print product

