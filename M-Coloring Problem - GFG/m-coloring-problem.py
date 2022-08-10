#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    color = [0] * V
    if solve(0, color, k, V, graph):
        return True
    
    return False


def solve(node, color, m, N, graph):
    if node == N:
        return True
   
    for i in range(1, m+1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            if solve(node+1, color, m, N, graph):
                return True
            color[node] = 0
    
    return False

def isSafe(node, color, graph, N, col):
    for i in range(0, N):
        if i!=node and graph[i][node]==1 and color[i]==col:
            return False
    
    return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends