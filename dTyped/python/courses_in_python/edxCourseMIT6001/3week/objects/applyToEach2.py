def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


testList = [1, -4, 8, -9]

def makePositive(n):
    return abs(n)

applyToEach(testList, makePositive)
print testList


testList = [1, -4, 8, -9]

def addone(n):
    return n + 1

applyToEach(testList, addone)
print testList


testList = [1, -4, 8, -9]

def square(n):
    return n * n

applyToEach(testList, square)
print testList
