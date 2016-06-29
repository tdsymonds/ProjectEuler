# https://projecteuler.net/problem=28

# first need to calculate how many diagonal numbers
# make up a 1001 by 1001 spiral.
length_of_spiral = 1001
number_of_layers = (length_of_spiral + 1) / 2
loop_to = (number_of_layers - 1) * 4 + 2

# set original values
previous_num = 1
sum_diagonals = 1

# loop and calculate the sum
for i in range(2, loop_to):
    new_num = previous_num + (2 * ((i + 2) // 4))
    sum_diagonals += new_num
    previous_num = new_num

# print result
print sum_diagonals
