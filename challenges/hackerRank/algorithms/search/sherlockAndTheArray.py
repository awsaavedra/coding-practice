#Solved naively, then looked up examples. This one is the most elegant
#NOTE: getting a linear solution is easy, getting space complexity down is harder
#Analysis:  Time complexity: O(n), space complexity: O(1)

def arraySherlock(a):   
    
    left_idx = 0
    right_idx = len(a) - 1
     
    left_sum = a[left_idx]
    right_sum = a[right_idx]
     
    while left_idx != right_idx:
        if left_sum < right_sum:
            left_idx += 1
            left_sum += a[left_idx]
        else:
            right_idx -= 1
            right_sum += a[right_idx]
     
    return left_sum == right_sum
     
if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        a = map(int, raw_input().split())
        if arraySherlock(a):
            print "YES"
        else:
            print "NO"
