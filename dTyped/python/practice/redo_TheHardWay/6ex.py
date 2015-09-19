x = "There are %s types of people" % 10
binary = "binary"
do_not = "don't" 
y = "Those who %s and those who do %s" % ( binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'."  % y

hilarious = False
joke_eval = "Isn't this a funny joke?! %r"

print joke_eval % hilarious

w = "This is the left side..."
s = "and this is the right side."

print w + s
