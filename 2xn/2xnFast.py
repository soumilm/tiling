import sys

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

def convertFromBit(arr):
    binary = 0
    for i in arr:
        binary = 2 * binary + i
    return binary

class Tiles:
    def __init__(self, top, mid, bottom, rotate=True):
        self.top = top
        self.mid = mid
        self.bottom = bottom
        self.rotate = rotate
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
        if self.rotate:
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
        if self.rotate:
            return self.hashHelp() + self.flipV().hashHelp() + self.flipH().hashHelp() + self.flipV().flipH().hashHelp()
        else:
            return self.hashHelp()

def convertToBit(n, len):
    arr = [0] * len;
    for i in range(len):
        r = n%2
        arr[i] = r
        n = (n - r)//2
    return arr

def findAll(n, bool, rotate=True):
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
                tile = Tiles(convertToBit(i, n-1), convertToBit(j, n), convertToBit(k,n-1), rotate)
                if (tile.checkRectangular() and tile not in all):
                    all.add(tile)
                    if (bool):
                        tile.display()
    if not bool and 2**(3*n-2) > 10**5:
        print()
    return len(all)

n = 0
if (len(sys.argv) > 1):
    n = int(sys.argv[1])
else:
    n = int(input("n = "))

display = False
if (len(sys.argv) > 2):
    display = bool(sys.argv[2])

rot = True
if (len(sys.argv) > 3):
    rot = bool(sys.argv[3])

total = findAll(n, display, rot)
print("Total tilings: ", end="")
print(total)