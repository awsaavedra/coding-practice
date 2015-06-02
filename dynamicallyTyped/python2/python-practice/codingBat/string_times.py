'''
string_times('Hi', 2) 'HiHi'
string_times('Hi', 3) 'HiHiHi'
string_times('Hi', 1) 'Hi'
'''

#using less built in Python exploits
def string_times(str, n):
  output = str
  for x in xrange(0,n-1):
    output += str
  print output

#More elegant solution
def string_times2(str,n):
  output = str*n
  print output

string_times('Hi', 2)
string_times('Hi', 3)
string_times('Hi',1)

print "\nSimpler way\n"
string_times2('Hi', 3)
string_times2('Hi', 2)