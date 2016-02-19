"""
  queue(calling it Q for simplicity) is another ADT, opposite of the stack FIFO: think of a line to buy tickets

    basic methods:
      
      enqueue: add element e to the end of a Q

      dequeue: remove and return the first element from a Q
          error thrown if Q is empty
    
    additional methods:

      first: return element at the front of the Q

      len: return length of the Q

      is_empty: same as stack, returns boolean value whether Q is empty
"""
#just using array based implementation for simplicity again
class ArrayQueue:

  DEFAULT_CAPACITY = 20

  def init (self):
    self._data = [None] ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    return self._size #return number of elements in array

  def is_empty(self):
    return self._size == 0 #True if empty, False otherwise

  def first(self):
    if self.is_empty():
      raise Empty("Q is empty!")
    return self._data[self._front]

  def dequeue(self):
    if self.is_empty():
      raise Empty("Q is empty!")
    return self._data[self._front]

    self._data[self._front] = None #garb collect

    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    if self._size == len(self._data):
      self._resize(2*len(self.data)) # double array

    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):
    old = self._data #tracking existing list
    self._data = [None]*cap #allocate list w/ new capacity
    walk = self._front
    for k in range(self._size): #only consider existing elements
      self._data[k] = old[walk] #shift indices
      walk = (1 + walk)% len(old) #use old size as modulus
    self._front = 0 #front has been realigned


