#User function Template for python3


class Solution:
    def kadanes(self,arr, n):
        s, maxi = arr[0], arr[0]
        
        for i in range(1,n):
            s += arr[i]
            s = max(s,arr[i])
            maxi = max(s,maxi)
        
        return maxi
        
        
    def maximumSumRectangle(self,R,C,M):
        res = M[0][0]
        
        for starti in range(R):
            subMatSum = [0 for _ in range(C)]
            for i in range(starti, R):
                for j in range(C):
                    subMatSum[j] += M[i][j]
        
                res = max(res, self.kadanes(subMatSum, C))
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends