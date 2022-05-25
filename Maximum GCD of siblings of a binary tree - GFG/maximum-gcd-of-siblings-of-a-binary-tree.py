#User function Template for python3
import math

class Solution:
    def maxBinTreeGCD(self, arr, N):
        GCD = 0
        maxGCD = 0
        arr = sorted(arr)
        
        for i in range(len(arr)-1):
            if arr[i][0] == arr [i+1][0]:
                GCD = math.gcd(arr[i][1], arr[i+1][1])
            else:
                continue
            
            maxGCD = max(GCD, maxGCD)
        
        return maxGCD

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from math import gcd
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        
        for i in range(N-1):
            u,v=map(int,input().split())
            arr.append([u,v])
        
        ob = Solution()
        print(ob.maxBinTreeGCD(arr,N))
# } Driver Code Ends