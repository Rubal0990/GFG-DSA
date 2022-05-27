#User function Template for python3
import math

class Solution:
	def numAndDen(self, n, d):
		num = -1
		den = 1
		
		for y in range(d+1, 10001):
		    x = (n * y) // d
		    if math.gcd(x, y) == 1:
		        if 1.0 * x / y > 1.0 * num / den:
                    num = x
                    den = y
        
        return [num, den]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,d = input().split()
		n=int(n)
		d=int(d)
		ob = Solution();
		ans = ob.numAndDen(n,d)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends