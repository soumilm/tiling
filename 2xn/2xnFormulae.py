import sys

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

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

print(total(n))
