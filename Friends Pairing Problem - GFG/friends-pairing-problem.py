#User function Template for python3
M = (10**9) + 7

class Solution:
    def countFriendsPairings(self, n):
        a0, a1 = 1, 1
        
        for i in range(2, n+1):
            a0, a1 = a1, ((i-1) * a0 % M + a1) % M
        
        return a1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends