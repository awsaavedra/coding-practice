#Purpose: Writes one file to another

from sys import argv
from os.path import exists #What does this do...

script, from_file, to_file = argv

#print "Copy from %s to %s" % (from_file, to_file)

#could put all this on one line, how?
# input = open(from_file)
# indata = input.read()

#indata = open(from_file).read() #equivalent? 

#print "The input file is %d bytes long." % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#raw_input("Ready, hit RETURN to continue or CTRL^C to abort.")


open(to_file, 'w').write(open(from_file).read())

#open(to_file,'w').write(indata)

#print "Alright, all done."

open(to_file).close()
open(from_file).close()