 #User function Template for python3
 
class Solution:
    def findLongestConseqSubseq(self, arr, N):
        arrSet = set(arr)
        longest = 0
        
        for i in arr:
            if i-1 not in arrSet:
                length = 0
                while i+length in arrSet:
                    length += 1
                
                longest = max(length, longest)
            
        return longest
        

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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends