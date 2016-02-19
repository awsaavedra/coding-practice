def isStrFunny(s):
    sLen = len(s)
    indx = 0
    while indx < sLen//2:
        left_diff = abs(ord(s[indx]) - ord(s[indx+1]))
        right_diff = abs(ord(s[sLen-indx-1]) - ord(s[sLen-indx-2]))
        if left_diff != right_diff:
            return False
        indx += 1
     
    return True
     
 
if __name__ == '__main__':
    t = input()
    for _ in range(t):
        s = raw_input()
        if isStrFunny(s):
            print "Funny"
        else:
            print "Not Funny"
