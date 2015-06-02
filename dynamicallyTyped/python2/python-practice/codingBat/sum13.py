"""
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 13 is very unlucky, so it does not count and numbers that 
come immediately after a 13 also do not count. 

sum13([1, 2, 2, 1]) => 6
sum13([1, 1]) => 2
sum13([1, 2, 2, 1, 13]) => 6
sum13([13, 1, 2, 13, 2, 1, 13])  => 3
sum13([5, 13, 2]) => 5  
"""
def sum13(nums):
  for i in range(0,len(nums)-1):
    if nums[i] >= 13:
      nums[i] = 0
      nums[i+1] = 0
  if nums[len(nums)-1] >= 13:
    nums[len(nums)-1] = 0 
  print sum(nums)

sum13([1, 2, 2, 1])
sum13([1, 1])
sum13([1, 2, 2, 1, 13])
sum13([13, 1, 2, 13, 2, 1, 13])
sum13([1, 2, 13, 2, 1, 13])
sum13([5, 13, 2])