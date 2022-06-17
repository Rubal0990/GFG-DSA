#User function Template for python3
class Solution:
    def areIsomorphic(self, str1, str2):
        dict1 = {}
        dict2 = {}
        
        for i, value in enumerate(str1):
            dict1[value] = dict1.get(value, []) + [i]
        
        for j, value in enumerate(str2):
            dict2[value] = dict2.get(value, []) + [j]
            
        if sorted(dict1.values()) == sorted(dict2.values()):
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends