def gcdIter(a, b):
  gcd = min(a,b)

  while gcd > 0:
    if (a%gcd) == 0 and (b%gcd) == 0:
      return gcd
    else:
      gcd -= 1

print gcdIter(2,12)
