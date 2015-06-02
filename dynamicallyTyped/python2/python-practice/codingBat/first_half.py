#return first half of a string

def first_half(str):
  str = raw_input("> ")
  if len(str) >= 2:
    length = len(str)
    half = str[0:length/2]
    print half
  else:
    print "please input a string of length >=2  "
first_half("filler")