"""
Return the number of times that the string "hi" appears 
anywhere in the given string. 

count_hi('abc hi ho') => 1
count_hi('ABChi hi') => 2
count_hi('hihi') => 2
"""
#simpler way
def count_hi2(str):
  print str.count('hi')

#less built ins
def count_hi(str):
  count = 0
  for i in range(0,len(str)-1):
    #need
    if str[i] == "h" and str[i+1] == "i" and str[i] != "H" and str[i+1] !="I":

      count += 1
  print count

count_hi('abc hi ho')
count_hi('ABChi hi')
count_hi('hihi')
