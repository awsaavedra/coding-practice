school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)

print "\n --------------------------- next-------------------"
#range(start, stop, stepSize)

divisor = 2
for num in range(0, 10, 2):
    print num/divisor 

print "\nnext---------------------"

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable % 16 == 0:
        print 'Foo!' 

print "\nnext2 -----------------------"
count = 0
for letter in 'Snow!':
    print 'Letter # ' + str(count) + ' is ' + str(letter)
    count += 1
    break
print count 

print "\n next3 -------------------- "
num = 10
for num in range(5):
    print num
print num

print "\n--------------next4-----------------"

num = 2
for i in range(2,11,2):
    print num
    num += 2
print "Goodbye!"
