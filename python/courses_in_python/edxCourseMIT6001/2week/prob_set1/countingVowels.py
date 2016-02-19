'''Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print: NUM OF VOWELS 5'''
s = 'azcbobobegghakl'
count = 0
vowels = ['a' , 'e' , 'i' ,'o' , 'u'] #array of vowels
for char in s:
	if char in vowels: #if characters in your string are also in vowels array
		count += 1

print("number of vowels: " + str(count))
