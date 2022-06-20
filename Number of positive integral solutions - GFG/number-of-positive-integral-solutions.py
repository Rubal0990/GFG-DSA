#User function Template for python3
from functools import lru_cache

class Solution:
    def posIntSol(self, s):
        left, right = s.split('=')
        k = int(right)
        n = len(left.split('+'))
        
        @lru_cache(None)
        def count(n, k):
            if k < n:
                return 0
          
            if n == 1:
                return int(k > 0)

            v = 0
            minv, maxv = 1, k - n+1
            for x in range(minv, maxv+1):
                v += count(n-1, k-x)
            return v
            
        return count(n, k)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.posIntSol(s))
# } Driver Code Ends