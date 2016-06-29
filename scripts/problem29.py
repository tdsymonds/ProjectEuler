# https://projecteuler.net/problem=29

results = []

for a in range(2,101):
    for b in range(2,101):
        results.append(a ** b)

results_set = set(results)
print len(results_set)