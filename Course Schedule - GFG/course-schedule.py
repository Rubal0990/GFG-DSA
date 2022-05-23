#User function Template for python3
from collections import deque

class Solution:
    def findOrder(self, n, m, prerequisites):
        graph = [[] for i in range(n)]
        
        for dest,src in prerequisites:
            graph[src].append(dest)
        
        indegree = [0 for i in range(n)]
        for i in graph:
            for j in i:
                indegree[j] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        if len(q) == 0:
            return []
        
        ans = []
        while(q):
            size = len(q)
            while(size):
                ele = q.pop()
                ans.append(ele)
                for nbrs in graph[ele]:
                    indegree[nbrs] -= 1
                    if indegree[nbrs] == 0:
                        q.append(nbrs)
                size-=1
        
        if len(ans) == n:
            return ans
        else:
            return []

#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
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
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends