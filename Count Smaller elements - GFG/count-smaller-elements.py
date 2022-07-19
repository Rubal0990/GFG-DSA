#User function Template for python3
import bisect
from collections import namedtuple 

Pair = namedtuple("Pair", ["value", "index"])

class Solution:
	def constructLowerArray(self,arr, n):
		pairs = sorted([Pair(value, index) for index, value in enumerate(arr)], key=lambda p: (-p[0], -p[1]))
		indexs = []
		ans = [0] * n
		
		for value, index in pairs:
		    right = n - index - 1
            i = bisect.bisect(indexs, index)
            big_right = len(indexs) - i
            ans[index] = right - big_right
            indexs.insert(i, index)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends