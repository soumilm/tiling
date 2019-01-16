def add(bools):
  tot = 0
  for i in bools:
    tot += i
  return tot;

def checkRepeat(arr, config):
  for i in arr:
    n = len(i)
    running = True
    for j in range(0, n):
      if i[j] != config[n-1-j]:
        running = False
        break
    if running:
      return True
  return False

def getValid(blocks, cuts):
  arr = [];
  num = blocks - 1;
  for i in range(0, 2**num):
    k = i
    rep = [0]*num
    j = 0
    cutsSoFar = 0
    while (k > 0):
      bit = k%2
      cutsSoFar += bit
      rep[j] = bit
      k = k//2
      j += 1
    if (cutsSoFar == cuts and not checkRepeat(arr, rep)):
      arr.append(rep)
  return arr

def displayCut(arr):
  print("|", end="_")
  for i in arr:
    if i == 1:
      print("|", end="_")
    else:
      print(" ", end="_")
  print("|")
  print()

def displayCuts(n, cuts):
  for i in getValid(n, cuts):
    displayCut(i)

def displayAll(n):
  for i in range(0, n):
    displayCuts(n, i)

displayAll(7)
