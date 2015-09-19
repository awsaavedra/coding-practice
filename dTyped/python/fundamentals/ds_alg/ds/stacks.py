"""
  Stacks: think of stacking books, pez dispensers, etc.
    -known as a LIFO (last in, first out) data structure

    -the simplest data structure, it is an ADT (abstract data type)

    core methods always used: 

      -push: add an element onto the top of the stack

      -pop: removes an element at the top of a stack

    additional methods:

      -top: returns a reference to the top of the stack (sometimes called peek) 
        w/o removing it

      -is_empty(): returns a boolean whether the stack is empty or not

      -len(stackName): returns the number of elements in a stack
"""

class ArrayStack:

  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)

  def is_empty(self):
    return len(self._data) == 0

  def push(self, e):
    self._data.append(e)

  def top(self):
    if self.is_empty():
      raise Empty(Stack is empty)
    return self._data[-1]

  def pop(self):
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._data.pop()


#example of using a stack
S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop( ))
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
