# https://projecteuler.net/problem=14

def increase_n(n):
    # if even
    if n % 2 == 0:
        return n/2
    # else odd
    return 3*n+1

# set initial variables
longest_chain = 0
number_with_longest_chain = 0

# for numbers up to a million
for i in range(1,1000000):
    # set n as i
    n = i
    # reset counter
    counter = 1
    # implement Collatz sequence
    while n != 1:
        n = increase_n(n)
        # increase counter
        counter += 1

    # if the longeset sequence then
    # update the variables
    if counter > longest_chain:
        longest_chain = counter
        number_with_longest_chain = i

# print result
print '%s [%s]' % (number_with_longest_chain, longest_chain)
