#User function Template for python3

class Solution:
    def count(self, S, m, n):
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
           
        for r in range(1, m+1):
            for c in range(1, n+1):
                if S[r-1] <= c:
                    dp[r][c] = dp[r][c - S[r-1]] + dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c]
       
        return dp[-1][-1]
   
    def recursive(self, S, m, n):
        if m == 0 and n > 0:
            return 0
       
        if n == 0:
            return 1
           
        if S[m-1] <= n:
            return self.count(S, m, n-S[m-1]) + self.count(S, m-1, n)
        else:
            return self.count(S, m - 1, n)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends