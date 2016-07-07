# https://projecteuler.net/problem=63

# set counter to 0
counter = 0

# not the most mathematical approach, but 
# loop to a large number and see if the 
# n digit numbers stop appearing (they do)
for i in range(1,100):
    # set initial variables
    j = 1
    x = j**i
    # while the number of digits in x
    # is less than or equal to i
    while len(str(x)) <= i:
        # if the length of x = i then bingo!
        if len(str(x)) == i:
            # increase counter
            counter += 1
            # print to observe weather numbers stop
            # occuring for large values
            print '[%s] : %s' % (i, x)

        # increment and recaclculate x
        j += 1
        x = j**i
        

# print result
print '--------------------------------'
print 'Total: %s' % (counter)
