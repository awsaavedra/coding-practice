print "Hello!"
num = 10
for i in range(0,10,2):
    print num
    num -= 2

print "\n ----------------summation loop----------------------"

end = 6
res = 0
for i in range(0,end+1):
	res = res + i
print res == 21

print " \n -----------------------"

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1



print "\n--------------------------count2--------------------"

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 


print "\n--------------------------count2--------------------"

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 
