from collections import deque

class Solution:
    def topoSort(self, V, adj):
        vis = [0] * (V)
        cou = [0] * (V)
        for i in adj:
            for j in i:
                cou[j] += 1
        
        q = deque()
        for i in range(V):
            if cou[i] == 0:
                q.append(i)
        
        ans = []
        while len(q) != 0:
            cur = q.popleft()
            ans.append(cur)
            for j in adj[cur]:
                cou[j] -= 1
                if cou[j] == 0:
                    q.append(j)
        
        return ans


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Endss