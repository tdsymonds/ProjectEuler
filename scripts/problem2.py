#https://projecteuler.net/problem=2

#set initial Fibonacci numbers
this_value = 2
last_value = 1

sum_even_values = 0

while (this_value < 4000000):

    if this_value % 2 == 0:
        #even number so sum
        sum_even_values += this_value
    
    # need to temp allocate this value to 
    # prev value so not lost
    prev_value = this_value

    # update Fibonacci numbers for next iteration
    this_value = this_value + last_value
    last_value = prev_value
    
print sum_even_values
