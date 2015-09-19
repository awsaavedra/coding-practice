ten_things = "Apples oranges Crows Telephone Light sugar"

print " Wait, that's not 10 things..."

stuff = ten_things.split(' ')
more_stuff = [ "Day", "Night", "Song", "Frisbee", "Corn", "Girl", "Boy"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print "Adding: ", next_one 
  stuff.append(next_one)
  print "There's %d items now." % len(stuff)

print "There we go: ", stuff
print "Let's do some thing with stuff."

print stuff[1]
print stuff[-1] # woah, fancy
print stuff.pop()
print ' '.join(stuff) #What? Cool
print '#'.join(stuff[3:5]) #super stellar!
