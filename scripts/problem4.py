#https://projecteuler.net/problem=4

pali_list = []

# Starting at 999, loop in reverse to 100
for x in range(999, 100, -1):
    # Sub loop from 999 in reverse
    for y in range(999, 100, -1):
        # mutliply x and y
        ans = x * y
        # convert to string for palidrome checks
        ans_string = str(ans)
        #split in half and compare part 1 and part 2
        part1 = ans_string[:3]
        part2 = ans_string[3:]

        if part1 == part2[::-1]:
            # palidrome found so add to list    
            pali_list.append(ans)

# print max value found
print max(pali_list)
