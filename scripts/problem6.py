#https://projecteuler.net/problem=6

sum_of_squares = 0
sum_of_nums = 0

for i in range(1,101):
	# calculate sum of squares
    sum_of_squares += i ** 2
    # calculate sum of numbers
    sum_of_nums += i

# square the sum
squareOfTheSum = sum_of_nums ** 2

# print difference
print squareOfTheSum - sum_of_squares
