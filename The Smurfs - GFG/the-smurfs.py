#User function Template for python3
from collections import Counter

class Solution:
    def minFind(self, n, a):
        c = Counter(a)
        
        if len(c) == 1: 
            return list(c.values())[0]
        
        if c['R']%2 == c['B']%2 and c['B']%2 == c['G']%2:
            return 2
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        
        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends