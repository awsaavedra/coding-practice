'''
Write an iterative function iterPower(base, exp)
'''

def iterPower(base,exp):  
  if exp == 0: 
    return 1
  else:
    temp = 1
    for x in range(exp):
      temp *= base
    return temp
    
#print iterPower(2,4)
print iterPower(-9.06, 7)
