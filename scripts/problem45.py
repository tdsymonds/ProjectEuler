# https://projecteuler.net/problem=45

def get_numbers(num_from, num_to):
    """
    A function to return a dict of all the
    triangle, pentagonal and hexagonal numbers
    in the range of the parameters.
    """
    number_dict = {'t':[], 'p':[], 'h':[]}

    for n in range(num_from, num_to+1):
        number_dict['t'].append(n*(n+1)/2)
        number_dict['p'].append(n*(3*n-1)/2)
        number_dict['h'].append(n*(2*n-1))

    return number_dict


# get the numbers for a large range
numbers = get_numbers(1, 100000)

# return the intersection of the lists, i.e. the numbers that are in all three.
numbers_in_all = list(set(numbers['t']) & set(numbers['p']) & set(numbers['h']))

# get the position of the number we know
i = numbers_in_all.index(40755)

# print the next number in the list
print numbers_in_all[i+1]


