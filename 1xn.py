def total(n):
  half = n//2
  total = pow(2, n-1)
  sym = pow(2, half)
  asym = (total - sym)//2
  return sym + asym

for n in range(2, 13):
  print(n, end=": ")
  print(total(n));
