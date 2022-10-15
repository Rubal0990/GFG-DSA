#User function Template for python3

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        N, M = len(grid), len(grid[0])
        MOVE_X = [1, -1, 0, 0]
        MOVE_Y = [0, 0, 1, -1]
        BLOCKED = 0
        queue = deque([(source, 0)])
        grid[source[0]][source[1]] = BLOCKED
        
        while queue:
            (x, y), cost = queue.popleft()
            if [x, y] == destination:
                return cost
            
            for delX, delY in zip(MOVE_X, MOVE_Y):
                newX = x + delX
                newY = y + delY
                
                if not (0<=newX<N) or not (0<=newY<M):
                    continue
                
                if grid[newX][newY] == BLOCKED:
                    continue
                
                grid[newX][newY] = BLOCKED
                queue.append(((newX, newY), cost + 1))
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends