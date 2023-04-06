# User function Template for python3

class Solution:
    def equalSum(self, A, N):
        l = 0
        h = N - 1
        m = 0
        
        while l <= h:
            m = (l + h) // 2
            
            if sum(A[:m+1]) == sum(A[m:]):
                return m + 1
                
            elif sum(A[:m+1]) >= sum(A[m:]):
                h = m - 1
                
            else:
                l = m + 1
                
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends