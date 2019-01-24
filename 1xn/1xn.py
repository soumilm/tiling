import sys

def total(n):
  half = n//2
  total = pow(2, n-1)
  sym = pow(2, half)
  asym = (total - sym)//2
  return sym + asym

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

for i in range(1, n+1):
  print(i, end=": ")
  print(total(i));
