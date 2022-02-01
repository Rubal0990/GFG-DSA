from heapq import *

class Solution:
    def dijkstra(self, N, m, s):
        heap = []
        heappush(heap, (0, s))
        dist = [float('inf') for _ in range(N)]
        dist[s] = 0
        
        while heap:
            (d, node) = heappop(heap)
            for (child, c) in m[node]:
                if dist[child] > (c+d):
                    dist[child] = c+d
                    heappush(heap, (dist[child], child))
        
        return dist

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends