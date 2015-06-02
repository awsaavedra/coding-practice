filename = raw_input("Please give me the filename you would like to open:")
txt = open(filename)

print "Here's your file %r:" % filename 
print txt.read() 

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read() 

txt.close() #How do I use this .close() method goddamn it?
txt_again.close()

print "What is the close variable boolean value?" + closed