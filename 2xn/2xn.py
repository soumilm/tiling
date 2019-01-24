import sys
import json

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

config = json.load(open('default.json'))
if (len(sys.argv) > 2):
    config = json.load(open(sys.argv[2]))

def strToBool(str):
    if str.lower() == "false":
        return False
    if str.lower() == "true":
        return True
    return bool(str)

# helper functions to dipsplay tilings
def displayH(bit):
    if (bit == 1):
        print("_", end="")
    else:
        print(" ", end="")
def displayV(bit):
    if (bit == 1):
        print("|", end="")
    else:
        print(" ", end="")

# helper for hash function
def convertFromBit(arr):
    binary = 0
    for i in arr:
        binary = 2 * binary + i
    return binary

# define class for configuration
class Tiles:
    def __init__(self, top, mid, bottom):
        self.top = top
        self.mid = mid
        self.bottom = bottom
        self.n = len(mid)

    def display(self):
        displayV(0)
        for _ in range(self.n):
            displayH(1)
            displayV(0)
        print()
        displayV(1)
        for i in range(self.n - 1):
            displayH(self.mid[i])
            displayV(self.top[i])
        displayH(self.mid[self.n - 1])
        displayV(1)
        print()
        displayV(1)
        for i in range(self.n - 1):
            displayH(1)
            displayV(self.bottom[i])
        displayH(1)
        displayV(1)
        print()
    
    def checkRectangular(self):
        for i in range(self.n - 1):
            if self.mid[i] != self.mid[i+1]:
                if self.top[i] * self.bottom[i] == 0:
                    return False
            if self.top[i] != self.bottom[i]:
                if self.mid[i] * self.mid[i+1] == 0:
                    return False
        return True

    def flipV(self):
        return Tiles(self.bottom, self.mid, self.top)

    def flipH(self):
        return Tiles(self.top[::-1], self.mid[::-1], self.bottom[::-1])

    def equal(self, another):
        if self.top != another.top:
            return False
        if self.mid != another.mid:
            return False
        if self.bottom != another.bottom:
            return False
        return True

    def __eq__(self, another):
        if self.equal(another):
            return True
        if config['rotate']:
            if self.flipH().equal(another):
                return True
            if self.flipV().equal(another):
                return True
            if self.flipH().flipV().equal(another):
                return True
        return False
    
    def hashHelp(self):
        temp = convertFromBit(self.top) * convertFromBit(self.mid) * convertFromBit(self.bottom)
        return temp % 2**(3*n)
    def __hash__(self):
        if config['rotate']:
            return self.hashHelp() + self.flipV().hashHelp() + self.flipH().hashHelp() + self.flipV().flipH().hashHelp()
        else:
            return self.hashHelp()

# helper function for interator below
def convertToBit(n, len):
    arr = [0] * len;
    for i in range(len):
        r = n%2
        arr[i] = r
        n = (n - r)//2
    return arr

# iterator function to find all tilings
def findAll(n):
    print("Total configurations to check", end=": ")
    print(2**(3*n - 2))
    all = set()
    counter = 0
    for i in range(2**(n-1)):
        for j in range(2**n):
            for k in range(2**(n-1)):
                counter += 1
                if (counter%(10**5) == 0 and not bool):
                    print("\rConfigurations checked so far: " + str(counter), end="")
                tile = Tiles(convertToBit(i, n-1), convertToBit(j, n), convertToBit(k,n-1))
                if (tile.checkRectangular() and tile not in all):
                    all.add(tile)
                    if (config['display']):
                        tile.display()
    if not bool and 2**(3*n-2) > 10**5:
        print()
    return len(all)

total = findAll(n)
print("Total tilings: ", end="")
print(total)
