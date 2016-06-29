# https://projecteuler.net/problem=26

# Solved using approach described here, using long division. 
# https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence

# Unfortunately takes about 60 minutes to run, which breaks the golden one minute rule :(
# The recurring sequence could be improved to reduce this time, but I'd rather crack on 
# with another solution.

# There are some really efficient and elegent solutions in the answer thread, which put
# mine to shame :)


def concatenate_two_integers(int1, int2):
    if not int1:
        return str(int2)

    int1_string = str(int1)
    int2_string = str(int2)
    return int1_string + int2_string

def last_digit(number):
    return int(number[-1])

def recurring_sequence(value_list):
    """
    A function to find and return the length of the recurring
    sequence (if there is one) in the list.
    """
    found = False
    # need more than one elment in list
    if len(value_list) > 1:
        for i in range(0,len(value_list)):
            if found:
                break

            # set initial variables
            left_mark = value_list[i]
            first_match = None
            match_list = [(i+1)*0]
            j = i

            for elm in value_list[i+1:]:
                right_mark = elm

                if left_mark == first_match:
                    found = True
                    break

                if left_mark == right_mark:
                    match_list.append(1)
                    if not first_match:
                        first_match = elm
                    # move left match over
                    j += 1
                    try:
                        left_mark = value_list[j]
                    except IndexError:
                        # end of the list
                        break

                else:
                    match_list.append(0)
                    # clear first match
                    first_match = None
                    # reset left mark
                    j = i
                    left_mark = value_list[j]

    return sum(match_list)

def long_division(dividend, divisor):
    """
    Simulates long division and calls the recurrence
    sequence formula to calculate the peroid length
    of a recurrence (if there is one)
    """

    # set initial variables
    dividend_string = str(dividend)
    digit = int(dividend_string[0])
    
    answer = None
    decimal = None
    difference = 1
    recurrence_length = 0
    digit_list = []
    period = 0
    i = 0

    while i < len(dividend_string):

        answer = concatenate_two_integers(answer, digit // divisor)
        remainder = digit % divisor

        number_under = last_digit(answer) * divisor

        # add digit to the list and calculate the 
        # recurring sequence if more than one elm
        # in the list.
        digit_list.append(digit)
        if len(digit_list) > 1:
            period = recurring_sequence(digit_list)
            if period > 0:
                # found a recurring sequence so 
                # break out of loop
                break
        
        difference = digit - number_under

        if i < len(dividend_string) - 1:
            # skip last iteration
            digit = int(concatenate_two_integers(digit - number_under, dividend_string[i+1]))
        
        elif difference != 0:
            # iterated through all the dividend digits and still
            # not solved.
            if not decimal:
                # if haven't already, note the place of the decimal point
                decimal = i + 1

            # add a zero to the end of the dividend string
            dividend_string = dividend_string + '0'
            # get digit
            digit = int(concatenate_two_integers(digit - number_under, 0))

        # increase i
        i+=1
    
    # if there's a decimal point we need to add it back in
    if decimal:
        return [period, '%s.%s' % (int(str(answer)[:decimal]), str(answer)[decimal:])]
    
    return [period, int(answer)]




# loop through each divisor / denominator
results_dict = {}
for divisor in range(2, 1000):
    results = long_division(1, divisor)
    results_dict[divisor] = results[0]
    print 'd: %s, period: %s, answer: %s' % (divisor, results[0], results[1])

# Confirm the max value
max_key = max(results_dict, key=results_dict.get)
print 'Longest recurring cycle: %s with a period of: %s' % (max_key, results_dict[max_key])
