#dictionary problems 

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

"""
First, write a procedure, called howMany, 
which returns the sum of the number of values associated with a dictionary."""

def howMany(aDict):
  count = 0
  for key in aDict:
    if len(aDict[key]) > 1:
      count += len(aDict[key])
    elif len(aDict[key]) == 1:
      count += 1
  return count
#print howMany(animals)

"""
This time, write a procedure, called biggest, which returns the key 
corresponding to the entry with the largest number of values associated 
with it. If there is more than one such entry, return 
any one of the matching keys."""

def biggest(aDict):

  biggest = 0
  biggestKey = []
  
  if len(aDict) == 0:
    return None
  for key in aDict:
    if len(aDict[key]) >= biggest:
      biggest = len(aDict[key])
      biggestKey = key
  print biggestKey

biggest(animals)
