# https://projecteuler.net/problem=30

# set initial variables
grand_sum = 0

# get powers for each digit
powers = { str(x): x**5 for x in range(0,10)}

# loop up to a large number (appreciate this
# isn't the most mathematical approach)
for i in range(10, 1000000):
    # set number variables
    num = i
    num_sum = 0
    # convert num to a list
    digit_list = list(str(num))
    # loop through each digit in the list
    for digit in digit_list:
        # sum up the digit to the 5th power
        num_sum += powers[digit]

    # if the num equals the num_sum
    # we have a match!
    if num == num_sum:
        # so add num to grand sum
        grand_sum += num

# print result
print grand_sum