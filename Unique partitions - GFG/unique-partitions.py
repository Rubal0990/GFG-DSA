#User function Template for python3

class Solution:
	def __init__(self):
        self.res = []

    def solve(self, n, pat, sum1):
        if sum1 < 0 or n <= 0:
            return
        
        if sum1 == 0:
            self.res.append(pat)
            return
        
        self.solve(n, pat+[n], sum1-n)
        self.solve(n-1, pat, sum1)

    def UniquePartitions(self, n):
        self.solve(n, [], n)
        return self.res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.UniquePartitions(n)
		for a in ans:
			for b in a:
				print(b, end = " ")
		print()

# } Driver Code Ends