#Animal is-a object (yes, sort of confusing) look at the extra credit
#REMEMEBER: CLASS INHERITS FROM A CLASS NAMED OBJECT 'object', just Python mistake
#multiple composition: has-many
#multiple inheritance: is-many 'multiple inheritance'
class Animal(object):
  pass

#class dog is-a animal
class Dog(Animal):

  def __init__(self, name):
    #self has-a name
    self.name = name

#class cat is-a animal
class Cat(Animal):

  def __init__(self, name):
    #self has-a name
    self.name = name

class Person(object):

  def __init__(self, name):
    #self has-a name
    self.name = name

    #person has-a pet of some kind
    self.pet = name
#employee is-a person
class Employee(Person):

  def __init__(self, name, salary):
    ## hmm, what is this strange magic?
    #...That's how you can run the __init__ method of a parent class reliably.
    #Google: Python super...
      #http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods 
    super(Employee, self).__init__(name)
    ##??
    self.salary = salary

class Fish(object):
  pass

#class salmon is-a fish 
class Salmon(Fish):
  pass

#class halibut is-a fish
class Halibut(Fish):
  pass

#rover is-a Dog object
rover = Dog("Rover")

# satan is-a cat object
satan = Cat("Satan")

# mary is-a person object
mary = Person("Mary")

mary.pet = satan

#initialize the employee frank to name = Frank, salary = 120000
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

#flipper is-a fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a halibut
harry = Halibut()