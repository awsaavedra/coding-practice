"""
extra_end('Hello') ->'lololo'
extra_end('ab') ->'ababab'
extra_end('Hi') -> 'HiHiHi'
"""
def extra_end(str):
  
  if len(str) >= 2:
    a = str[0:2]
    print a+a+a

  else:
    print "input should be a string  of len >=2"

extra_end(raw_input("> "))