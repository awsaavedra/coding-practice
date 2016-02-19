"""
Given a string, return a string where for every char in the original, 
there are two chars. 

double_char('The') => 'TThhee'
double_char('AAbb') => 'AAAAbbbb'
double_char('Hi-There') => 'HHii--TThheerree'
"""

def double_char(str):
  duplicate_letter = ""
  duplicate_str = ""
  for i in range(0, len(str)-1):
    duplicate_letter = str[i]+str[i]
    duplicate_str += duplicate_letter
  print duplicate_str

double_char('The')
double_char('AAbb')
double_char('Hi-There')