# https://projecteuler.net/problem=52

def has_same_digits(number_list):
    """
    Returns true if all the numbers in the list
    are made up of the same digits.
    """
    # get the first number as a sorted list
    first_sorted_number_list = sorted(str(number_list[0]))
    
    # loop through the remaining numbers in the list
    for number in number_list[1:]:
        # if this number list sorted does not equal
        # the first sorted number
        if sorted(str(number)) != first_sorted_number_list:
            # number digits don't match
            return False

    # all match
    return True

# set variables
i = 0
found = False

# loop until found
while not found:
    # increment i
    i += 1
    # create number list and check if same digits
    found = has_same_digits([x * i for x in range(2, 7)])

# print result
print i