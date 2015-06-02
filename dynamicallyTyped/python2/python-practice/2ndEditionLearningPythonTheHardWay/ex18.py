def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r and arg2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
  print "args1: %r amd arg2: %r" % (arg1, arg2)

def print_one(arg1):
  print "args1: %r" %arg1

def print_none():
  print "I got nothing!"

print_two("Alex", "Saavedra")
print_two_again("Alex", "Saavedra")
print_one("Only!")
print_none()