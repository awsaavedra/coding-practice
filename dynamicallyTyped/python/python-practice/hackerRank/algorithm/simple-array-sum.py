def sum_array(ar):
  arSplit = ar.split()
  l = len(arSplit)
  
  sum = 0
  for x in range(1,l):
    sum = sum + int(arSplit[x])
  print sum
sum_array("6\n1 2 3 4 10 11")


