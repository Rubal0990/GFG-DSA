#User function Template for python3
from itertools import accumulate

class Solution:	
	def wineSelling(self, Arr, N):
		prefix = list(accumulate(Arr))
	    return sum(abs(num) for num in prefix)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr,N)
        
        print(ans)

# } Driver Code Ends