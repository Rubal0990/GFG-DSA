#User function Template for python3

class Solution:
    def countOfNodes(self, graph,n):
        even = 1
        odd = 0
        q = []
        q.append(1)
        flag = True
        visited = {1}
        
        while q:
            p = []
            while q:
                poped = q.pop(0)
                for i in graph[poped]:
                    if i not in visited:
                        p.append(i)
                        visited.add(i)
            if flag:
                odd += len(p)
                flag = False
            else:
                even += len(p)
                flag = True
            q = p
            
        return ((even) * (even - 1) // 2) + ((odd) * (odd - 1) // 2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = input().split()
        graph = defaultdict(list)
        for i in range(0,2*n-2,2):
            graph[int(arr[i])].append(int(arr[i+1]))
            graph[int(arr[i+1])].append(int(arr[i]))
            
            
        
        ob = Solution()
        print(ob.countOfNodes(graph,n))
# } Driver Code Ends