my_name = "Alexander Saavedra"
my_age = 24
my_height = 68
my_weight = 140
my_eyes = "hazel"
my_teeth = "white"
my_hair = "brown"

print "Let's talk about %s." %my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, tryto get it exactly right

print "If I add %d, %d, and %d I get %d." %( 
	my_age, my_height, my_weight, my_age + my_height + my_weight )