#User function Template for python3
class Solution:
    def check(self, N, M, Edges): 
        def backtrack( s, visited, adj, counter, v):
            if counter == v:
                return True
            
            visited[s] = True
            
            for neighbour in adj[s]:
                if not visited[neighbour] and backtrack(neighbour, visited, adj, counter+1, v):
                    return True
            
            visited[s] = False
            
            return False
        
        adj = [[] for i in range(N+1)]
        v = N
        for edge in Edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = [False]*(v+1)
        
        for i in range(1,v):
            if not visited[i] and backtrack(i, visited, adj, 1, v):
                return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends