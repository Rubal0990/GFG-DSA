#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		n = len(str)
		p = str 
		m = [[0  for i in range(n+1)] for i in range(n+1)]
		
		for i in range(n+1):
		    for j in range(n+1):
		        if i == 0 or j == 0:
		            m[i][j] = 0
		
		for i in range(1, n+1):
		    for j in range(1, n+1):
		        
		        if str[i-1] == p[j-1] and i != j:
		            m[i][j] = m[i-1][j-1] + 1
		        else:
		            m[i][j] = max(m[i-1][j], m[i][j-1])
		
		return m[n][n]
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends