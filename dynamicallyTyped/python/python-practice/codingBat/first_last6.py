'''
Given an array of ints, return True if 6 appears as either the first or 
last element in the array. The array will be length 1 or more. 

first_last6([1, 2, 6]) => True
first_last6([6, 1, 2, 3]) => True
first_last6([13, 6, 1, 2, 3]) => False
'''
#just access start and end of array, no need to loop
def first_last6(nums):
  sixHere = False
  start = nums[0]
  end = nums[len(nums)-1]
  if start == 6:
    sixHere = True
  if end == 6:
    sixHere = True
  else:
    sixhere = False
  print sixHere

first_last6([1, 2, 6]) 
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3]) 