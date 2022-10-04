# User function Template for Python3
from collections import defaultdict
class node:
    def __init__(self):
        self.child = defaultdict(node)
        self.c = 0

class Solution:
    def prefixCount(self, N, Q, li, query):
        root = node()
        for w in li:
            r = root
            for i in w[0]:
                r = r.child[i]
                r.c += 1
        
        res = []
        for w in query:
            r = root
            for i in w[0]:
                r = r.child[i]
            res.append(r.c)
        
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        li = []
        for i in range(N):
            li.append(input().split())
        Q = int(input())
        query = []
        for i in range(Q):
            query.append(input().split())
        
        ob = Solution()
        ans = ob.prefixCount(N, Q, li, query)
        for i in range(Q):
            print(ans[i])
# } Driver Code Ends