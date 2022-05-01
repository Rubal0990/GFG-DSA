# User function Template for python3

class Solution:
    def equilibriumPoint(self,A, N):
        mid = N//2
        left = 0
        right = 0
        
        for i in range(mid):
            left += A[i]
            
        for i in range(N-1, mid, -1):
            right += A[i]
        
        if right > left:
            while right > left and mid < N-1:
                right -= A[mid+1]
                left += A[mid]
                mid += 1
        else:
            while left > right and mid > 0:
                right += A[mid]
                left -= A[mid-1]
                mid -= 1
                
        if right == left:
            return mid + 1
        else:
            return -1

#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends