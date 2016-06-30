# https://projecteuler.net/problem=31

def number_of_sums(coin_list, target_value):
    # first create a list starting at 1
    # followed by the rest in zeros
    num_of_solutions = [1] + [0] * target_value

    # loop through each coin in the coin list
    for index, coin in enumerate(coin_list):
        while coin <= target_value:
            num_of_solutions[coin] += num_of_solutions[coin - coin_list[index]]
            # increment coin by 1 to keep list shifting 
            # towards the end of the list.
            coin += 1

    # return the last value in the list
    return num_of_solutions.pop()


# define variables
coin_list = [1,2,5,10,20,50,100,200]
target_value = 200

# call function and print
print number_of_sums(coin_list, target_value)
