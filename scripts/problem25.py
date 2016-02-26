# https://projecteuler.net/problem=25

# set target length
length_to_find = 1000

# set starting length
length = 0

# starting term number
term = 2

# set starting fib numbers
n_minus_2 = 0
n_minus_1 = 1


# loop until found
while True:

   # calculate n 
   n = n_minus_1 + n_minus_2

   # calculate length
   length = len(str(n))

   if length == length_to_find:
      # found so break the loop
      break
   
   # set previous values for next loop
   n_minus_2 = n_minus_1
   n_minus_1 = n

   # increase term count
   term += 1

# print the result
print term
