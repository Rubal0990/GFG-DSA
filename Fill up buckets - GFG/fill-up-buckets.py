#User function Template for python3

class Solution:
	def totalWays(self, n, capacity):
		res = 1
		M = 10**9 + 7
		capacity.sort()
		
		for i in range(n):
		    res = (res * (capacity[i] - i)) % M
		
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		capacity = list(map(int,input().split()))
		ob = Solution()
		ans = ob.totalWays(n,capacity)
		print(ans)

# } Driver Code Ends