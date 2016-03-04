# https://projecteuler.net/problem=17

# dictionary for parsing numbers to words
num_word_dict = { 
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 
    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
    
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 
    60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
}


# a simple recursion function to change all numbers from 1 to 1000
# into words
def number_in_words(number):

    if (0 < number < 20):
        return num_word_dict[number]
    
    elif (20 <= number < 100):
        tens, single_digit_num = divmod(number, 10)        
        return num_word_dict[tens * 10] + ' ' + number_in_words(single_digit_num)

    elif (100 <= number < 1000):
        hundreds, double_digit_num = divmod(number, 100)
        if double_digit_num == 0:
            return num_word_dict[hundreds] + ' Hundred'
        return num_word_dict[hundreds] + ' Hundred and ' + number_in_words(double_digit_num)

    elif (number == 1000):
        return 'One Thousand'

    # return an empty string for one hundred etc.
    return ''
        

# set starting total length
total_length = 0

# loop through each number in range 1 to 1000
for i in range(1, 1001):
    # remove the spaces
    n = number_in_words(i).replace(' ', '')
    # add the length to total length
    total_length += len(n)

# print answer
print total_length
