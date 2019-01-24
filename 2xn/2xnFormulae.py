# Algebraic solutions to the number of ways to tile a 2xn grid

import sys

# Total number of tilings
# Counts different reflections and rotations as distinct
def total(n):
    count = [1]
    i = 1
    while i <= n:
        sum = 0
        for k in range(1, i+1):
            sum += (3**(k-1) + 1) * count[i-k]
        count.append(sum)
        i += 1
    return count
def prettyPrintTotal(n):
    counts = total(n)
    for i in range(len(counts)):
        print(i, end=':\t')
        print(counts[i])

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

prettyPrintTotal(n)
