#User function Template for python3

class Solution:
	def digitsNum(self, N):
		res = '0' * N
        q, r = divmod(N, 9)
        return (str(r) + '9'*q + res).lstrip('0')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.digitsNum(n)
		print(ans)
# } Driver Code Ends