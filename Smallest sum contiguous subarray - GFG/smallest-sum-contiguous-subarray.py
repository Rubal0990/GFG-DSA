#User function Template for python3

class Solution:
    def smallestSumSubarray(self, A, N):
        currMax = 0
        res = 999999 
        
        for i in range(N):
            currMax += A[i]
            res = min(res, currMax)
            
            if currMax > 0:
                currMax = 0
        
        return res    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends