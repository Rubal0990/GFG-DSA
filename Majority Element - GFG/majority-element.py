#User function template for Python 3
from collections import Counter

class Solution:
    def majorityElement(self, A, N):
        if len(A) == 1:
            return A[0]
        
        if len(set(A)) == len(A) or len(A) == 2:
            return -1
        
        for key, val in Counter(A).items():
            if val > N/2:
                return key
        
        return -1


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
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends