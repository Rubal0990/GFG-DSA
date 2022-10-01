#User function Template for python3

class Solution:
    def bfsOfGraph(self, V, adj):
        queue = [0]
        visited = [0]
        
        while queue:
            popVertex = queue.pop(0)
            
            for neighbour in adj[popVertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        
        return visited


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends