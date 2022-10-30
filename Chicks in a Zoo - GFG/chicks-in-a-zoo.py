#User function Template for python3

class Solution:
	def NoOfChicks(self, N):
		p = []
        for i in range(0, N+1):
            p.append(1)
        
        q, p[0] = 1, 1
        
        for i in range(1, N):
            if i >= 6:
                q -= p[i-6]
            
            p[i] =  2 * q
            q += p[i]
        
        return q


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		obj = Solution()
		ans = obj.NoOfChicks(N)
		print(ans)

# } Driver Code Ends