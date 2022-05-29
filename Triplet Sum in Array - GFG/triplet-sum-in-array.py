#User function Template for python3

class Solution:
    def find3Numbers(self, A, n, X):
        A.sort()
        
        for i in range(n-2):
            l = i + 1
            r = n - 1
            
            while l < r:
                if A[i] + A[l] + A[r] == X:
                    return 1
                elif A[i] + A[l] + A[r] < X:
                    l += 1
                elif A[i] + A[l] + A[r] > X:
                    r -= 1
            
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends