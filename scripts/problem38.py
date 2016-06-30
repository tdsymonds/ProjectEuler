# https://projecteuler.net/problem=38

# set variables
largest_pandigital = 0
numbers_one_to_nine = [str(x) for x in range(1,10)]

# loop through numbers in range
for i in range(1, 10000):

    # reset break variable
    number_too_large = False

    # loop through multiplication list values
    for j in range(2,10):

        # stops unneccesary looping through
        # larger mutliplication lists
        if number_too_large:
            break

        # create multiplication list
        mutiplication_list = range(1,j)

        # initialise empty variable
        pandigital = ''

        # loop through each num in multiplication list
        for k in mutiplication_list:
            
            # if the answer is longer than 9 digits
            # then break out to the next number.
            if len(pandigital) > 9:
                number_too_large = True
                break

            # add to pandigital variable
            pandigital += str(k * i)

        # get the integer number and the ordered list of the numbers
        pandigital_num = int(pandigital)
        pandigital_list = sorted(pandigital)

        # is the pandigital of length 9, larger than the current 
        # largest and contains all the digits one to nine?
        if len(pandigital) == 9 and pandigital_num > largest_pandigital and pandigital_list == numbers_one_to_nine:
            largest_pandigital = pandigital_num


# print answer
print largest_pandigital


