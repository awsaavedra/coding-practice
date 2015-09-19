'''
Write a Python function that returns a list of keys in aDict with the 
value target. The list of keys you return should be sorted in increasing 
order. The keys and values in aDict are both integers. 
(If aDict does not contain the value target, you should return an empty list.)
'''
d = {1:1, 2:2, 3:3, 4:3, 5:3}
def keysWithValue(aDict, target):
    #variable for list of keys
    for k, v in aDict.iteritems():
        #if the value is equal to target
          #append the value to the list of keys
    #return the sorted list of keys
