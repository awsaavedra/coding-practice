"""
Given 3 int values, a b c, print their sum. However, if one of the values is 
the same as another of the values, it does not count towards the sum. 

lone_sum(1, 2, 3) ==> 6
lone_sum(3, 2, 3) ==> 2
lone_sum(3, 3, 3) ==> 0
"""
#probably going to look for an easy method for containment
def lone_sum(a,b,c):
  count = 0
  if a != b and a != c and b != c:
    print a+b+c
  elif a == b and a != c and b != c:
    print c
  elif a != b and a == c and b != c:
    print b
  elif a != b and a != c and b == c:
    print a
  else:
    print 0


lone_sum(1, 2, 3)
lone_sum(3, 2, 3)
lone_sum(3, 3, 3)