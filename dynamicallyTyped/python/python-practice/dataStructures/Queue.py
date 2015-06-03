"""
Array based queue, FIFO: think of a line of people
Fundamental Methods:

  Q.enqueue(e): Add element e to the back of queue Q.

  Q.dequeue(): Remove and return the first element from queue Q;
  an error occurs if the queue is empty.

Supporting methods:

  Q.first( ): Return a reference to the element at the front of queue Q,
  without removing it; an error occurs if the queue is empty.

  Q.is_empty( ): Return True if queue Q does not contain any elements.

  len(Q): Return the number of elements in queue Q; in Python,
  we implement this with the special method len .
"""
class Queue:
  DEFAULT_SIZE = 10

  #initializes the empty queue
  def __init__(self):
    self._data = [None].Queue.DEFAULT_SIZE
    self._size = 0
    self._front = 0

  def __len__(self):
    return self._size #returning length of the queue

  def is_empty(self):
    if self._size == 0:
      return True
    else:
      return False

  def first(self):
  #returns front element in queue
    if self.is_empty():
      raise Empty("Queue is Empty")
    return self._data[self._front]

  def dequeue(self): 
  #returns first element of queue, raises exception if queue is empty
    if self.is_empty( ):
      raise Empty( "empty queue" )
    result = self._data[self._front] 
    self._data[self._front] = None #for garbage collection
    self._front = (self._front+1)%len(self._data)
    self._size -= 1 #decrement size of queue
    return result

  def enqueue(self, e):
  #adding elements to the back of the queue
    queueLength = len(self._data)
    if self._size == queueLength:
      self._resize(2*queueLength)
    #space available in queue
    available = (self._front + self._size) % queueLength 
    self._data[available] = e 
    self._size += 1 #increment queue size by one
  def resize(self, cap): #assuming cap >= len(self)
    #going to resize to capacity >= len(self)
    oldList = self._data #so we have old lists size available
    self._data = [None]*cap #create list with new capacity
    walker = self._front
    for i in range(0,self._size):
      self._data[i] = oldList[walker] #shifting all indices
      walker = (1+walker)%len(oldList)
    self._front = 0 #front is reassigned to 0

# Q = Queue() #instantiate the Queue class
# Q.enqueue(5) #add to the queue
# Q.enqueue(3) 
# print len(Q) 
# Q.dequeue() #remove elements at head of the queue
# print Q.is_empty() #false, since queue is not empty
# Q.dequeue() 
# print Q.is_empty() #true, since both added elements are gone
# print Q.dequeue() #raises error, queue is empty
# Q.enqueue(7)
# Q.enqueue(9)
# Q.first() #returns 7
# Q.enqueue(4)
# print len(Q) #length should be 3
# Q.dequeue() #remove head of line, 7