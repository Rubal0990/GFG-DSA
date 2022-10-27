#User function Template for python3

class Solution:
	def NthTerm(self, n):
	    mod = 10**9 + 7
	    sum = 1 
		    
	    for i in range(1, n+1):
	        sum = ((sum* i)%mod + 1)%mod
	    
	    return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends
