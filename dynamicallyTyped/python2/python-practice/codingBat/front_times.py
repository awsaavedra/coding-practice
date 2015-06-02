'''
front_times('Chocolate', 2) >'ChoCho'
front_times('Chocolate', 3) > 'ChoChoCho'
front_times('Abc', 3) > 'AbcAbcAbc'
'''

def front_times(str, n):
  substring = str[0:3]
  result = substring
  for x in xrange(0,n-1):
    result += substring
  print result

front_times('Chocolate', 2)
front_times('Chocolate', 3)
front_times('Abc', 3)