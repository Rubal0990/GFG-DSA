class Solution:
    def soln(self,s,t,i,j,dp):
        if i==0 or j==0:
            return max(i, j)
        
        if dp[i][j] != -1:
            return dp[i][j]
        else:
            if s[i-1] == t[j-1]:
                dp[i][j] = self.soln(s, t, i-1, j-1, dp)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(self.soln(s, t, i-1, j-1, dp), self.soln(s, t, i, j-1, dp), self.soln(s, t, i-1, j, dp))
            
            return dp[i][j]
    
	def editDistance(self, s, t):
        # Code here
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        
        return self.soln(s, t, n, m, dp)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends