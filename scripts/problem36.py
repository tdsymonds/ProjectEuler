# https://projecteuler.net/problem=36

def is_palindrome(number_string):
    """
    Returns true if a number is a palindrome.
    """
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


# reset total
total = 0

# loop through range to 1 million
for i in range(1, 1000000):
    # if both the number and binary number are palindromes
    if is_palindrome(str(i)) and is_palindrome('{0:b}'.format(i)):
        # add i to total
        total += i

# print result
print total