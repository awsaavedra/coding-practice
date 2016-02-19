"""
Return True if the given string contains an appearance of "xyz" 
where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not. 

xyz_there('abcxyz') => True
xyz_there('abc.xyz') => False
xyz_there('xyz.abc') => True
"""

def xyz_there(str):
  #avoiding tranversing through the whole string
  if str[0:3] == "xyz":
    print True
  for i in range(0,len(str)-1):
    if str[i] != "." and str[i+1:i+4] == "xyz":
      print True
  print False

xyz_there('abcxyz')
xyz_there('abc.xyz')
xyz_there('xyz.abc')