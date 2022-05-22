class Solution:
    def mergesort(self,arr,n,inv):
        if n == 1:
            return 0
        
        mid = n // 2
        l = arr[:mid]
        r = arr[mid:]
        LeftLen = len(l)
        RightLen = len(r)
        inv += self.mergesort(l, LeftLen, inv) + self.mergesort(r, RightLen, inv)
        i, j, k = 0, 0, 0
        
        while i < LeftLen and j < RightLen:
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
                inv += mid - i
            k += 1
            
        while i < LeftLen:
            arr[k] = l[i]
            i += 1
            k += 1
            
        while j < RightLen:
            arr[k] = r[j]
            j += 1
            k += 1
            
        return inv
        
    def inversionCount(self, arr, n):
        inv = 0
        return self.mergesort(arr, n, inv)

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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends