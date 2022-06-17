class Solution:
	def isBipartite(self, V, adj):
		colors = {}
		
        def color(n, c):
            if n in colors:
                return colors[n] != 1-c
            
            colors[n] = c
            for nbr in adj[n]:
                if not color(nbr, 1-c):
                    return False
            return True
            
        for i in range(len(adj)):
            if i in colors:
                continue
            if not color(i, 0):
                return False

        return True

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends