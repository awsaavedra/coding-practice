'''
operations: insertion, iterate, complex keys

remember: keys must be immutable
'''
dict = { 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
print(dict[1])
print(dict)

collect = []
for e in dict:
	collect.append(e)

print(collect)
