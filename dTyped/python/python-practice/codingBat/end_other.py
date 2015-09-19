"""
Given two strings, return True if either of the strings appears at 
the very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string. 

end_other('Hiabc', 'abc') => True
end_other('AbC', 'HiaBc') => True
end_other('abc', 'abXabc') => True
"""

#using built in functions for simplicity
def end_other(str1, str2):
  str1Lower = str1.lower() #turns all string values into lower case ASCII values
  str2Lower = str2.lower()
  if str1Lower.endswith(str2Lower):
    print True
  elif str2Lower.endswith(str1Lower):
    print True
  else:
    print False

#less built in functions (I'll)

end_other('Hiabc', 'abc')
end_other('abc', 'abXabc')
end_other('AbC', 'HiaBc')
