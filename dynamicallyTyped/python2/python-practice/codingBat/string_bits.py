'''
Given a string, return a new string made of every other char starting with the first, 
so "Hello" yields "Hlo". 
string_bits('Hello') > 'Hlo'
string_bits('Hi') > 'H'
string_bits('Heeololeo') > 'Hello'
'''

def string_bits(str):
  result = ""
  for x in xrange(0,len(str)):
    if x % 2 != 1:
      result += str[x]
  print result

#elegant solution
def string_bits2(str):
  result = str[0:len(str):2]
  print result

string_bits('Hello')
string_bits('Hi')
string_bits('Heeololeo')
print '\n'
string_bits2('Heeololeo')