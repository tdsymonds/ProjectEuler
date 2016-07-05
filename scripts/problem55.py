# https://projecteuler.net/problem=55

def is_palindrome(number):
    """
    Returns true if a number is a palindrome.
    """
    number_string = str(number)
    number_length = len(number_string)
    
    # set the default cutpoints
    cutpoint = number_length / 2
    first_partition = number_string[:cutpoint]
    second_partition = number_string[cutpoint:]
    
    # if odd need to cut the middle number
    # out of the partitions
    if number_length % 2 != 0:
        second_partition = number_string[cutpoint + 1:]
    
    # do the partitions match?
    if first_partition == second_partition[::-1]:
        # have a palindrome!
        return True

    # no palindrome
    return False

    
# set initial variables
number_limit = 10000
lychrel_limit = 50
lychrel_number_counter = 0

# loop through each number up to limit
for i in range(1,number_limit+1):
    # assume lychrel until proven otherwise
    lychrel_number = True
    # set number variable
    num = i
    # loop for up to the limit of iterations
    for j in range(0,lychrel_limit):
        # reverse and add
        num += int(str(num)[::-1])
        # is the number a palindrome?
        palindrome = is_palindrome(num)
        # palindrone so break to next number
        if palindrome:
            lychrel_number = False
            break

    # if exhausted iterations and still not
    # found a palindrome then assume a lychrel
    # number
    if lychrel_number:
        # print i
        lychrel_number_counter += 1

# print result
print lychrel_number_counter
