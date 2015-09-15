"""
Write a function recurPower(base, exp) which compute
"""

def recurPower(base, exp):
  if exp == 0:
    return 1
  else:
    return base*recurPower(base, exp-1)

print recurPower(2,4)
