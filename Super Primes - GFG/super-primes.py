#User function Template for python3
class Solution:
    def superPrimes(self, n):
	    dp = [False] * (n+1)
	    
        for i in range(2, n+1):
            dp[i] = True
        
        p = 0
        while p*p <= n:
            if dp[p]:
                i = p*p
                while i<=n:
                    dp[i] = False
                    i += p
            p += 1
		
		ans = 0
		for i in range(5, n+1):
		    if dp[i] and dp[i-2]:
		        ans += 1
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.superPrimes(n)
		print(ans)

# } Driver Code Ends