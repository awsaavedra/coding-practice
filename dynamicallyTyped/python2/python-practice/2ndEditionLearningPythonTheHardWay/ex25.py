#Return to this problem, lots of functions to remember
print """
Instead of calling >>import ex25, use >>from ex25 import *
which is like saying, 'Import everything from ex25.'
"""

def break_words(stuff):
  """This function will break up words for us."""
  words = stuff.split(' ') #method: split()
  return words

def sort_words(words):
  """Sorts of Words"""
  return sorted(words) #method: sorted()

def print_first_word(words):
  """Prints the first word after popping it off."""
  word = words.pop(0) #method: pop()
  print word

def print_last_word(words):
  """Prints the last word after popping it off."""
  word = words.pop(-1) #method pop(), -1 meaning?
  print word

def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words"""
  words = break_words(sentence) #calls break method to break words apart to...
  return sort_words(words) #call sort method to sort the broken words in order

def print_first_and_last(sentence):
  """Prints the first and last words of the sentence"""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """Sorts the words then prints the first and last one."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)