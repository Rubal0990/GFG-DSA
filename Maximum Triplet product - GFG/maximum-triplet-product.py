#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        arr.sort(reverse = True)
        mx1 = 1
        for i in range(3):
            mx1 *= arr[i]
        
        mx2 = arr[0]
        arr.sort()
        for i in range(2):
            mx2 *= arr[i]
        
        if mx1 > mx2:
            return mx1
        
        return mx2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends