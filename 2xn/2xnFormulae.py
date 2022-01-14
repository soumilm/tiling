# Algebraic solutions to the number of ways to tile a 2xn grid

import sys

# Total number of tilings
# Counts different reflections and rotations as distinct

counts = [1,2,8]
def tilings(n):
    if (n < len(counts)): return counts[n]
    for i in range(len(counts), n+1):
        val = 6 * counts[i-1] - 7 * counts[i-2]
        counts.append(val)
    return counts[n]

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

tilings(n)

def horizontallySymmetric(i):
    if i == 0: return 1
    return 2 * (3 ** (i-1))
def verticallySymmetric(i):
    if i == 0: return 1
    k = i//2
    if (i % 2 == 0):
        return counts[k+1] - counts[k]
    else:
        return counts[k+1]
def rotationallySymmetric(i):
    if i == 0: return 1
    k = i//2
    if (i % 2 == 0):
        return 2 * counts[k]
    else:
        return counts[k+1]
def perfectlySymmetric(i):
    if i == 0: return 1
    k = i//2
    if (i % 2 == 0):
        return 4 * (3 ** (k-1))
    else:
        return 2 * (3 ** k)
def asymmetric(i):
    return (
        counts[i]
        - verticallySymmetric(i)
        - horizontallySymmetric(i)
        - rotationallySymmetric(i)
        + (2 * perfectlySymmetric(i))
    )
def equivalenceClasses(i):
    return (
        (asymmetric(i) // 4)
        + perfectlySymmetric(i)
        + (
            verticallySymmetric(i)
            + horizontallySymmetric(i)
            + rotationallySymmetric(i)
            - 3 * perfectlySymmetric(i)
        )//2
    )

print("Total (counting transformations as distinct) : " + str(counts[n]))
print("Total (counting transformations as identical): " + str(equivalenceClasses(n)))
