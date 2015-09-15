'''
A semordnilap is a word or a phrase that spells a different word when 
backwards ("semordnilap" is a semordnilap of "palindromes"). 
Here are some examples:
	nametag / gateman
	dog / god
	live / evil
	desserts / stressed
Write a recursive program, semordnilap, that 
takes in two words and says if they are semordnilap.
'''
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False
    if str1 == "" and str2 == "":
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:-1],str2[1:-1])
