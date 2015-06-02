'''
Given an array of ints, return the number of 9's in the array. 

array_count9([1, 2, 9]) > 1
array_count9([1, 9, 9]) > 2
array_count9([1, 9, 9, 3, 9]) > 3
'''
def array_count9(nums):
  count = 0
  if len(nums) <= 0:
    print "array length invalid"
    return 0
  for i in range(0,len(nums)):
    if nums[i] == 9:
      count += 1
  print count

array_count9([1, 2, 9])
array_count9([1, 9, 9])
array_count9([1, 9, 9, 3, 9])
array_count9([])