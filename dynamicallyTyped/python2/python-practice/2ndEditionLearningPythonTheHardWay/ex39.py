ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not ten things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "boy"]

while len(stuff) < 10:
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  stuff.append(next_one)
  print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do somethings with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff) #
print '#'.join(stuff[3:5]) #concatenate all string elements # inbetween

"""
Translate these two ways to view the function calls in English.
For example, ’ ’.join(things) reads as, “Join things with ‘ ‘ between 
them.” Meanwhile,  join(’ ’, things) means, “Call join with ‘ ‘ and 
things.” Understand  how they are really the same thing.

Q: What’s the relationship between dir(something) and the “class” of something?

A: dir(something) gives you all the attributes of the object. 
The class is like the blueprint for the house.
You can only use numbers to retrieve items from a list. 
You can use any type to retrieve items from a dictionary. 
For example: list[1] versus dictionary[‘word’].
"""

