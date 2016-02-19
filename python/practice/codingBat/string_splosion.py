'''
Given a non-empty string like "Code" return a string like "CCoCodCode". 
string_splosion('Code') >'CCoCodCode'
string_splosion('abc') >'aababc'
string_splosion('ab') >'aab'
'''
def string_splosion(str):
  result = ""
  for x in xrange(0,len(str)+1):
    result += str[0:x]
  print result
    
string_splosion('nahaman')
string_splosion('Code')
string_splosion('abc')
string_splosion('ab')
string_splosion('Alexander')