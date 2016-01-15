# https://projecteuler.net/problem=19

from datetime import datetime, date

# set starting point and end point
starting_year = target_year = 1901
starting_month = target_month = 1

ending_year = 2001
ending_month = 1

# set total to 0
total = 0

# create starting and end date
target_date = date(starting_year, starting_month, 1)
end_date = date(ending_year, ending_month, 1)

while (target_date < end_date):
    
    # date is a sunday so increment total
    if target_date.weekday() == 6:
        total += 1

    # returns the monnth and year based on the target month
    year, month = divmod(target_month, 12)

    # need to add 1 to the month, as above returns 0 - 11
    month += 1

    # increase target_date by a month 
    target_date = date(target_year + year, month, 1)

    # increase target month variable
    target_month += 1

print total
