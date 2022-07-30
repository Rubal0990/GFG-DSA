#User function Template for python3
from collections import Counter

class Solution:
    def firstRep(self, s):
        d = Counter(s)
        
        for i in s:
            if d[i] > 1:
                return i
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.firstRep(s)
        if ans is '#':
            print(-1)
        else:
            print(ans)
        
# } Driver Code Ends