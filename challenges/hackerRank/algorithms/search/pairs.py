#time: n*logn, space: O(n)

def pairs(a,k):
    ans = 0
    s = set(a)
    for i in s:
        if i + k in s:
            ans += 1
     
    return ans
if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    b = map(int, raw_input().split())
    print pairs(b, k)
