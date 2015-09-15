'''
Write a Python function that returns the sublist of strings in aList that 
contain fewer than 4 characters. For example, if 
aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]
'''
def lessThan4(aList):
  subList = []
  for word in aList:
		if len(word) < 4 and len(word) >= 0:
			subList.append(word)
  return subList
print lessThan4(["apple", "cat", "dog", "banana"])
