# https://projecteuler.net/problem=16

power = 1000
result = 2 ** power

# sum up digits
sum_result = 0
while result:
    sum_result += result % 10
    result //= 10
    
print sum_result

