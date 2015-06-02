class Parent(object): #creating class parent which inherits from class object (confusing thing in python)

  def override(self): #parent method override with parameter self
    print "PARENT override()" #prints a string to terminal
  def implicit(self): #parent method implicit with parameter self
    print "PARENT implicit()"
  def altered(self): #method altered with parameter self
    print "PARENT altered()"

class Child(Parent): #class child which inherits from parent 

  def override(self): #inherited method from parent which is override with parameter self
    print "CHILD override()"

  def altered(self): #method altered which was inherited from parent
    print "CHILD, BEFORE PARENT altered()"
    super(Child, self).altered() 
    #call super with arguments Child and self, then call the function altered on whatever it returns
    print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

print "-----------------------------------Composition -------------------------"

class Other(object):

  def override(self):
    print "OTHER override()"

  def implicit(self):
    print "OTHER implicit()"

  def altered(self):
    print "OTHER altered()"

class Child(object):

  def __init__(self):
    self.other = Other()

  def implicit(self):
    self.other.implicit()

  def override(self):
    print "CHILD override()"

  def altered(self):
    print "CHILD, before altered"
    self.other.altered()
    print "CHILD, after altered"

son = Child()

son.implicit()
son.override()
son.altered()