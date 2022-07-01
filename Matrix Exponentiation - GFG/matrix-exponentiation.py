#User function Template for python3
import numpy as np

M = 10 ** 9 + 7 
def exp(m, n):
    ans = np.eye(2, dtype=np.int_)
    
    while n:
        if n & 1:
            ans = (ans @ m) % M
        m = (m @ m) % M
        n >>= 1

    return ans % M

class Solution:
    def FindNthTerm(self, n):
		m = np.array([1, 1, 1, 0], dtype=np.int_).reshape(2, 2)
		p = exp(m, n-1)
		init = np.array([1, 1], dtype=np.int_).reshape(2, 1)
		return (p@init)[0][0] % M

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.FindNthTerm(n)
		print(ans)

# } Driver Code Ends