#dictionary is a collection of key value pairs
#unordered collections

months = { 'Jan': 1, 'Feb' : 2} #key: val
  #REMEMBER: keys are IMMUTABLE, so you can use tuples, etc. but NOT lists

for e in months:
  print months[e]

print "can do months.keys(): %s" % months.keys()


print "\n------------------------------- dictionary problem 1-------------\n"

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey' 

print animals

print animals['c']

#print animals['donkey'] #produces error, explain why.

print len(animals)

animals['a'] = 'anteater'

print animals['a']

print len(animals['a'])

print animals.has_key('baboon')

print 'donkey' in animals.values()

print animals.has_key('b')

print animals.keys()

del animals['b']

print len(animals)

print animals.values()
