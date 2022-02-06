import sys
util = __import__('2xnFormulae')

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

util.tilings(n)

output = "\n".join([str(util.equivalenceClasses(i)) for i in range(1, n+1)])

f = open("numbers.txt", "w")
f.write(output)
f.close()
