"""
a fixed array is a data structure whose value is fixed at runtime for instance
 array1 = [0,0,0]
  you cannot dynamically resize it

dynamic array

  dArray = [1,2,3]
  dArray.append(4)
  print dArray #[1,2,3,4]

Arrays allow random access, which in theory, means that any index within the 
array can be accessed in constant time O(1)
 
  pros:
    1. Arrays grant random access due to contiguous in memory property

    2. easy to add to the end 

  cons:

    1. poor insertion time within array

    2. resizing an array takes a lot of time
"""

import ctypes

class DynamicArray:

