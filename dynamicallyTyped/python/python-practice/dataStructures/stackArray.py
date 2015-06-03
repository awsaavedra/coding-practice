"""
Stacks are the simplest of all data structures, yet they are also among the most
important. They are used in a host of different applications, and as a tool for 
many more sophisticated data structures and algorithms. Formally, a stack is an 
abstract data type (ADT) such that an instance S supports the following two methods:

  S.push(e): Add element e to the top of stack S.

  S.pop( ): Remove and return the top element from the stack S;
  an error occurs if the stack is empty.

  Accessor methods for convenience:

  S.top( ): Return a reference to the top element of stack S, without
  removing it; an error occurs if the stack is empty.

  S.is empty( ): Return True if stack S does not contain any elements.

  len(S): Return the number of elements in stack S; in Python, we
  implement this with the special method len .By convention, we assume that a 
  newly created stack is empty, and that there is no a priori bound on
"""
class arrayStack:
  #A stack is a LIFO, last in first out storage system
  def __init__(self):
    self._data = [] #creating an empty array stack, not public 

  def __len__(self):
    numberOfElementsInStack = len(self._data)
    return numberOfElementsInStack 

  def is_empty(self): #whether stack is empty or not
    if len(self._data) == 0:
      return True
    else:
      return False
  def push(self, e):
    latestElement = self._data.append(e)
    return latestElement

  def top(self):
    #returns the last element added to the stack, doesn't remove
    empty = self.is_empty()
    if empty:
      raise Empty("Empty stack") #raises an except if stack is empty
    return self._data[-1] # last element in the list

  def pop(self):
    #same as top, except DOES remove last element
    if self.is_empty():
      raise Empty("Empty stack")
    return self._data.pop() #lastElement from list removed

#Testing stack
S = arrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)


