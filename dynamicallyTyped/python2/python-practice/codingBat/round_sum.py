"""
For this problem, we'll round an int value up to the next multiple of 10 
if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, 
round down to the previous multiple of 10 if its rightmost digit is less than 5, 
so 12 rounds down to 10. Given 3 ints, a b c, print the sum of their rounded 
values. To avoid code repetition, write a separate helper "def round10(num):" 
and call it 3 times. Write the helper entirely below and at the same indent 
level as round_sum(). 

round_sum(16, 17, 18) => 60
round_sum(12, 13, 14) => 30
round_sum(6, 4, 4) => 10
"""
def round_sum(a,b,c):

  sum_a = 0+round10s(a)
  sum_b = sum_a+round10s(b)
  sum_c = sum_b+round10s(c)
  print sum_c

def round10s(num):

  #ceiling
  if (num%10) > 4: #if the 1s place number is greater than 4
    ceiling = (num/10+1)*10 
    return ceiling
  #floor
  else:
    floor = (num/10)*10
    return floor
round_sum(16, 17, 18)
round_sum(12, 13, 14)
round_sum(6, 4, 4)