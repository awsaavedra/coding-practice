"""
Given 2 strings, a and b, return the number of the positions where they 
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since 
the "xx", "aa", and "az" substrings appear in the same place in both strings. 

string_match('xxcaazz', 'xxbaaz') => 3
string_match('abc', 'abc') => 2
string_match('abc', 'axc') => 0
"""

def string_match(a,b):
  shorterString = 0
  count = 0
  shorterString = min(len(a),len(b))
  for i in range(0,shorterString-1):
    a_sub = a[i]+a[i+1]
    b_sub = b[i]+b[i+1]
    if a_sub == b_sub:
      count += 1
  print count
  return count

string_match('xxcaazz', 'xxbaaz')
string_match('abc', 'abc')
string_match('abc', 'axc')