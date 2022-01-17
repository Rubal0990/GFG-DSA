#User function Template for python3
from collections import deque

class Solution:
    def closing (self,s, i):
        if s[i] != '[':
            return -1
    
        d = deque()
        
        for k in range(i, len(s)):
            if s[k] == ']':
                d.popleft()
            elif s[k] == '[':
                d.append(s[i])
                
            if not d:
                return k
    
        return -1
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    pos = int (input ())
    ob = Solution()
    print (ob.closing (s, pos))
    
# Contributed By: Pranay Bansal

# } Driver Code Ends