import sys
util = __import__('2xnFormulae')

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

util.tilings(n)

print("Total (counting transformations as distinct) : " + str(util.getCounts(n)))
print("Total (counting transformations as identical): " + str(util.equivalenceClasses(n)))
