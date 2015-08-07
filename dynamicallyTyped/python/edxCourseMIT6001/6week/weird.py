class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
#print w1.getX()

print '----------------------------------'

print w1.getY()


w2 = Wild(X, Y)
print w2.getX()
