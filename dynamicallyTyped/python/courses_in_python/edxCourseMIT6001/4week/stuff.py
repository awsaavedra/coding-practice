a = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
b = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
c = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
d = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
e = "iPad"
f = 'iPad'

stuff = f
for thing in stuff:
	if thing == 'iPad':
		print stuff 
		print "found it"
