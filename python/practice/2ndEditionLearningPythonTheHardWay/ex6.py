x = "There are %d types of people" % 10 #string w/n string
binary = "binary"
do_not = "don't"
#string w/n string
y = "Those that know %s and those that %s know binary" % (binary, do_not)

print x
print y

print "I said: %r." % x #string w/n string
print "I also said: '%s'. " % y #string w/n string

hilarious = False
joke_eval = "Isn't this joke funny?! %r" #string w/n string

print joke_eval % hilarious

a = "This is the left side of the string..."
b = "and this is the right side of the string"

print a + b