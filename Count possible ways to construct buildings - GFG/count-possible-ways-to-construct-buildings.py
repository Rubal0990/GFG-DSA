#User function Template for python3

class Solution:
	def TotalWays(self, N):
        m = (10 ** 9) + 7
	    dp =[0, 2, 3] + [0] * (N - 2)
	    
	    for i in range(3, N+1):
	        dp[i] = (dp[i-1] + dp[i-2]) % m
	        
        return (dp[N] * dp[N]) % m

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends