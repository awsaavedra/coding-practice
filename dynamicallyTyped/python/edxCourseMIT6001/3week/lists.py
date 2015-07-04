'''
lists are mutable
operations: append(), +, etc.
'''

Univs = ['MIT', 'Cal Tech', 'RPI', ['Harvard', 'Yale', 'Brown']]

for e in Univs:
	print('Univs contains ')
	print(e)
	print(' which contains')
	for u in e:
		print(' ' + u)
