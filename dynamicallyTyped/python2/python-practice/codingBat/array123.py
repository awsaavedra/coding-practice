'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array 
somewhere. 

array123([1, 1, 2, 3, 1]) > True
array123([1, 1, 2, 4, 1]) > False
array123([1, 1, 2, 1, 2, 3]) > True
'''
def array123(nums):
  is1234InArray = False
  for i in range(0,len(nums)-1):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      is1234InArray = True
  print is1234InArray
  
array123([1, 1, 2, 3, 1])
array123([1, 1, 2, 4, 1])
array123([1, 1, 2, 1, 2, 3])