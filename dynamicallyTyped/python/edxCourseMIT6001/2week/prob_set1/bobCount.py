'''
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print 2
'''
s = 'azcbobobegghakl'
l = len(s) #length of string s
count = 0
for i in range(l):
	if s[i:].startswith('bob'):
		count += 1

print( 'Number of times bob occurs is: ' + str(count))

print "\n alternatively doing the comparison in C"

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

print("C comparison, # of times bob occurs is: " + str(occurrences('azcbobobegghakl', 'bob')))
