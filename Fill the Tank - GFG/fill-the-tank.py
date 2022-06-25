#User function Template for python3
import sys
sys.setrecursionlimit(10**8)


class Solution:
    def minimum_amount (self, edges, N, S, cap):
        
        def recur(graph, visited, cur_node, cap):
            # If the current tank is visted we return -1
            if visited[cur_node]:
                return -1
                
            visited[cur_node] = True
            # Current capacity of the tank
            cur_cap = cap[cur_node-1]
            # Maximum capacity of it's neighbours
            max_neigh_cap = 0
            # Number of neighbours it has, apart from it's parents
            # From where it's water is coming
            neighbours = 0
            
            # Iterating through it's neighbours
            for neigh_node in graph[cur_node]:
                # Recursing through it's neighbours
                neigh_cap = recur(graph, visited, neigh_node, cap)
                # If the nieghbour is already visited we won't increase the
                # neighbour count
                if neigh_cap == -1:
                    continue
                # Taking the maximum of the neighbourse capacity
                max_neigh_cap = max(max_neigh_cap, neigh_cap)
                neighbours += 1
            
            # Increasing the current capacity by the maximum of neighbours
            # capacity times the number of neighbours
            cur_cap += max_neigh_cap * neighbours
            
            return cur_cap
            
        # Building Graph
        graph = {i: [] for i in range(1, N+1)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        # Visited Array
        visited = [False] * (N + 1)
        
        # DFS to find the capacity needed
        res = recur(graph, visited, S, cap)
        
        # If any tank is not visted meaning it was not filled, so we return -1
        for i in range(1, N+1):
            if not visited[i]:
                return -1
        
        # If the result is greater than total water, we return -1
        if res > 10 ** 18:
            return -1
            
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        num, start = map(int,input().split())
        Cap = list(map(int, input().split()))
        Edges = list()
        for i in range(0, num-1):
            L = list(map(int, input().split()))
            Edges.append(L)
        ans = ob.minimum_amount(Edges, num, start, Cap);
        print(ans)




# } Driver Code Ends