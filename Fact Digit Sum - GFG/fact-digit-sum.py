#User function Template for python3

class Solution:
    def fact(self, dc):
        dc[0] = 1
        
        for i in range(1, 10):
            dc[i] = i * dc[i-1]
        
	def FactDigit(self, N):
		dc = {}
		li = []
		self.fact(dc)
		keys = list(dc.keys())
		
		for i in range(len(keys)-1, -1, -1):
		    while N >= dc[i]:
		        N -= dc[i]
		        li.append(i)
		
        ans = reversed(li)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.FactDigit(N)
		for _ in ans:
			print(_, end = "")
		print()
# } Driver Code Ends