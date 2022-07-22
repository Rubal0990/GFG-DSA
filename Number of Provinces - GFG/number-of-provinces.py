#User function Template for python3
from collections import defaultdict

class Solution:
    def numProvinces(self, adj, V):
        g = defaultdict(list)
        for i, r in enumerate(adj):
            for j, v in enumerate(r):
                if i == j or v == 0:
                    continue
                g[i].append(j)
        
        seen = set()

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for nbr in g[i]:
                dfs(nbr)

        ans = 0
        for i in range(0, V):
            if i in seen:
                continue
            dfs(i)
            ans += 1
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends