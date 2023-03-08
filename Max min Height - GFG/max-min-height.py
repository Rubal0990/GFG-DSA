#User function Template for python3
from typing import List

class Solution():
    def isOK(self, arr: List[int], days: int, cs: int, h: int) -> bool:
        n = len(arr)
        waterSupply = [0] * n
        
        if arr[0] < h:
            waterSupply[0] = h - arr[0]
            days -= (h - arr[0])
        
        if days < 0:
            return False
        
        for i in range(1, n):
            waterSupply[i] = waterSupply[i-1]
            actualHeight = arr[i]
            
            if i >= cs:
                actualHeight += (waterSupply[i] - waterSupply[i-cs])
            
            else:
                actualHeight += waterSupply[i]
            
            if actualHeight < h:
                waterSupply[i] += (h - actualHeight)
                days -= (h - actualHeight)
            
            if days < 0:
                return False
        
        return True

    def maximizeMinHeight(self, n, k, w, a):
        res = -1
        mnHeight = min(a)
        mxHeight = (1 << 31) - 1
        
        while mnHeight <= mxHeight:
            guessHeight = (mxHeight + mnHeight) // 2
            
            if self.isOK(a, k, w, guessHeight) == True:
                res = guessHeight
                mnHeight = guessHeight + 1
            
            else:
                mxHeight = guessHeight - 1
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k,w = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(Solution().maximizeMinHeight(n, k, w,arr))

# } Driver Code Ends